#!/usr/bin/env python3
# coding: utf-8

import socket,platform,sys
from os import system,mkdir,getcwd
from data import version

# 获取系统平台架构
def get_host_arch():
    ar = platform.uname().machine
    if ar == 'x86_64':
        os = "amd64"
    elif ar == 'aarch64':
        os = 'arm64'
    return os


if get_host_arch() == 'amd64':
    from data.amd64 import images, raw, rpms
elif get_host_arch() == 'arm64':
    from data.arm64 import images, raw, rpms



current_dir = getcwd()
raw_save_dirname = current_dir+'/raw'
rpms_save_dirname = current_dir+'/rpms'
images_save_dirname = current_dir+'/images'

try:
    mkdir(raw_save_dirname)
    mkdir(rpms_save_dirname)
    mkdir(images_save_dirname)
except:
    pass

# 查询本机ip地址
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('114.114.114.114', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

#  公共参数
common = {
    'local_hostname': get_host_ip(),
    'repo_port': '8081',
    'registry_port': '8082',
    'architectures': get_host_arch(),
    'kube_version': sys.argv[1],
    'kube_upgrade_version': sys.argv[2]
}

kubeops_repo_amd64 = """
[Centos-Base]
name=CentOS Base
baseurl=http://{ip}:8081/repository/centos-base/7/extras/$basearch/
enabled=1
gpgcheck=0

[Centos-Extras]
name=CentOS Extras
baseurl=http://{ip}:8081/repository/centos-base/7/os/$basearch/
enabled=1
gpgcheck=0

[Centos-epel]
name=CentOS epel
baseurl=http://{ip}:8081/repository/centos-epel/7/$basearch/
enabled=1
gpgcheck=0
"""

kubeops_repo_arm64 = """
[Centos-Base]
name=CentOS Base
baseurl=http://{ip}:8081/repository/centos-altarch/7/extras/$basearch/
enabled=1
gpgcheck=0

[Centos-Extras]
name=CentOS Extras
baseurl=http://{ip}:8081/repository/centos-altarch/7/os/$basearch/
enabled=1
gpgcheck=0

[Centos-epel]
name=CentOS epel
baseurl=http://{ip}:8081/repository/centos-epel/7/$basearch/
enabled=1
gpgcheck=0
"""

gpu_repo = """
[Centos-CUDA]
name=CentOS CUDA
baseurl=http://{ip}:8081/repository/centos-cuda/rhel7/$basearch/
enabled=1
gpgcheck=0

[Centos-libnvidia-containe]
name=CentOS libnvidia-containe
baseurl=http://{ip}:8081/repository/libnvidia-container/centos7/$basearch/
enabled=1
gpgcheck=0

[Centos-nvidia-container-runtime]
name=nvidia-container-runtime
baseurl=http://{ip}:8081/repository/nvidia-container-runtime/centos7/$basearch
gpgcheck=0
enabled=1

[Centos-nvidia-docker]
name=nvidia-docker
baseurl=http://{ip}:8081/repository/nvidia-docker/centos7/$basearch
gpgcheck=0
"""


def create_yum_repo():
    if common.get('architectures') == "arm64":
        try:
            a_repo = open("/etc/yum.repos.d/kubeops.repo","w")
            ip = get_host_ip()
            a_repo.write(kubeops_repo_arm64.format(ip=ip))
        except IOError:
            print("Error: 没有找到文件或读取文件失败")
        else:
            print("kubeops.repo: 写入成功")

    if common.get('architectures') == "amd64":
        try:
            ip = get_host_ip()
            k_repo = open("/etc/yum.repos.d/kubeops.repo", "w")
            k_repo.write(kubeops_repo_amd64.format(ip=ip))
            g_repo = open("/etc/yum.repos.d/gpu.repo", "w")
            g_repo.write(gpu_repo.format(ip=ip))
        except IOError:
            print("Error: 没有找到文件或读取文件失败")
        else:
            print("gpu.repo: 写入成功")
            g_repo.close()
            k_repo.close()
    cmd = 'yum clean all && rm -rf /var/cache/yum/* && yum makecache'
    system(cmd)

def separate(v, n, t):
    print("********************",v,n,t,"********************",flush=True)


def download(k8s_version):
    try:
        clear_image = "docker system prune --all --volumes -f"
        system(clear_image)
    except SystemError:
        print("Error: 镜像清理失败")

    separate(k8s_version,'K8S image pull |',common.get('architectures'))
    for name, value in images.k8s_images.items():
        url = value
        k = dict()
        k.update(version.version_mg(k8s_version))
        k.update(common)
        url = url.format(**k)
        cmd_pull = 'docker pull '+url
        print('Command: ',cmd_pull)
        cmd_remove = 'docker rmi -f '+url
        system(cmd_pull)
        system(cmd_remove)
    print('\n')

    separate(k8s_version,'App image pull |',common.get('architectures'))
    for i in range(len(images.app_images)):
        k = dict()
        k.update(common)
        k.update(version.version_mg(k8s_version))
        m = images.app_images[i]
        for image in m:
            img = image.format(**k)
            cmd_pull = 'docker pull '+img
            print('Command: ',cmd_pull)
            cmd_remove = 'docker rmi -f '+img
            system(cmd_pull)
            system(cmd_remove)
            print('\n')

    separate(k8s_version,'Storage image pull |',common.get('architectures'))
    for name, value in images.storage_images.items():
        url = value
        k = dict()
        k.update(version.version_mg(k8s_version))
        k.update(common)
        url = url.format(**k)
        cmd_pull = 'docker pull '+url
        print('Command: ',cmd_pull)
        cmd_remove = 'docker rmi -f '+url
        system(cmd_pull)
        system(cmd_remove)
    print('\n')

    separate(k8s_version,'Raw downalod |',common.get('architectures'))
    for name, value in raw.raw_url.items():
        url = value
        k = dict()
        k.update(version.version_mg(k8s_version))
        k.update(common)
        url = url.format(**k)
        cmd = 'wget --timeout=600 -nv --no-check-certificate ' + url + ' -P '+ raw_save_dirname
        print('Command: ',cmd)
        system(cmd)
    print('\n')

    separate(k8s_version,'Rpm download |',common.get('architectures'))
    for rpm in rpms.rpms_base:
        cmd = 'yumdownloader --resolve --destdir=' + rpms_save_dirname + ' ' + rpm
        print('Command: ',cmd)
        system(cmd)
    print('\n')

    if common.get(k8s_version,'architectures')  == 'amd64':
        separate('NVIDIA rpm download |', common.get('architectures'))
        for rpm in rpms.rpms_gpu:
            cmd = 'yumdownloader --resolve --destdir=' + rpms_save_dirname + ' ' + rpm
            print('Command: ', cmd)
            system(cmd)
    print('\n')

    separate(k8s_version,'Download finished |',common.get('architectures'))

def run():
    create_yum_repo()
    kube_version = common.get('kube_version')
    kube_upgrade_version = common.get('kube_upgrade_version')
    download(kube_version)
    download(kube_upgrade_version)

