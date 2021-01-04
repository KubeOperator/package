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

kubeops_repo = """
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
    try:
        k_repo = open("/etc/yum.repos.d/kubeops.repo","w")
        ip = get_host_ip()
        k_repo.write(kubeops_repo.format(ip=ip))
    except IOError:
        print("Error: 没有找到文件或读取文件失败")
    else:
        print("kubeops.repo: 写入成功")
        k_repo.close()

    if common.get('architectures') == "amd64":
        try:
            g_repo = open("/etc/yum.repos.d/gpu.repo", "w")
            g_repo.write(gpu_repo.format(ip=ip))
        except IOError:
            print("Error: 没有找到文件或读取文件失败")
        else:
            print("gpu.repo: 写入成功")
            g_repo.close()
    cmd = 'yum clean all && yum makecache'
    system(cmd)

def separate(v, n, t):
    print("********************",v,n,t,"********************",flush=True)

# 下载
def download(kube_version, *args):
    separate(kube_version,'K8S image pull |',common.get('architectures'))
    for name, value in images.k8s_images.items():
        url = value
        k = dict()
        k.update(version.version_mg(kube_version))
        k.update(common)
        url = url.format(**k)
        cmd_pull = 'docker pull '+url
        cmd_remove = 'docker rmi -f '+url
        system(cmd_pull)
        system(cmd_remove)
    print('\n')

    separate(kube_version,'App image pull |',common.get('architectures'))
    for image in images.app_images:
        k = dict()
        k.update(common)
        k.update(version.version_mg(kube_version))
        img = image.format(**k)
        cmd_pull = 'docker pull '+img
        cmd_remove = 'docker rmi -f '+img
        system(cmd_pull)
        system(cmd_remove)
    print('\n')

    separate(kube_version,'Raw downalod |',common.get('architectures'))
    for name, value in raw.raw_url.items():
        url = value
        k = dict()
        k.update(version.version_mg(kube_version))
        k.update(common)
        url = url.format(**k)
        cmd = 'wget --timeout=600 -nv --no-check-certificate ' + url + ' -P '+ raw_save_dirname
        system(cmd)
    print('\n')

    # 下载升级离线包
    for v in args:
        separate(v, 'Raw downalod |', common.get('architectures'))
        for name, value in raw.raw_url.items():
            url = value
            k = dict()
            k.update(version.version_mg(v))
            k.update(common)
            url = url.format(**k)
            cmd = 'wget --timeout=600 -nv --no-check-certificate ' + url + ' -P ' + raw_save_dirname
            system(cmd)
        print('\n')

    separate(kube_version,'Rpm download |',common.get('architectures'))
    for rpm in rpms.rpms_base:
        cmd = 'yumdownloader --resolve --destdir=' + rpms_save_dirname + ' ' + rpm
        system(cmd)
    print('\n')

    if common.get('architectures')  == 'amd64':
        separate('NVIDIA rpm download |', common.get('architectures'))
        for rpm in rpms.rpms_gpu:
            cmd = 'yumdownloader --resolve --destdir=' + rpms_save_dirname + ' ' + rpm
            system(cmd)
    print('\n')

    separate(kube_version,'Download finished |',common.get('architectures'))

def run():
    create_yum_repo()
    kube_version = common.get('kube_version')
    download(kube_version)
