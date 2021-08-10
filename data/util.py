#!/usr/bin/env python3
# coding: utf-8

import socket, platform, sys
from os import system, mkdir, getcwd, popen
from data import version


# 获取系统平台架构
def get_host_arch():
    ar = platform.uname().machine
    if ar == 'x86_64':
        os = "amd64"
    elif ar == 'aarch64':
        os = 'arm64'
    return os


# 获取系统名称
def get_host_platform():
    plat = platform.platform()
    pl = ""
    if "centos" in plat.lower():
        pl = "centos"
    else:
        pl = 'ubuntu'
    print("当前系统为：", pl)
    return pl


if get_host_arch() == 'amd64':
    from data.amd64 import images, raw, rpms
elif get_host_arch() == 'arm64':
    from data.arm64 import images, raw, rpms

current_dir = getcwd()
raw_save_dirname = current_dir + '/raw'
rpm_save_dirname = current_dir + '/rpms'
images_save_dirname = current_dir + '/images'

try:
    mkdir(raw_save_dirname)
    mkdir(rpm_save_dirname)
    mkdir(images_save_dirname)
except:
    pass

#  公共参数
common = {
    'local_hostname': sys.argv[2],
    'repo_port': '8081',
    'registry_port': '8082',
    'architectures': get_host_arch(),
    'kube_version': sys.argv[1],
    'plat_form': get_host_platform(),
    'ubuntu_version': popen("cat /etc/lsb-release |grep DISTRIB_CODENAME|awk -F= '{print $2}'").read().strip(),
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

ubuntu_apt_amd64 = """
deb http://{ip}:8081/repository/apt-proxy-{ubuntu_version} {ubuntu_version} main restricted universe multiverse
deb http://{ip}:8081/repository/apt-proxy-{ubuntu_version} {ubuntu_version}-security main restricted universe multiverse
deb http://{ip}:8081/repository/apt-proxy-{ubuntu_version} {ubuntu_version}-updates main restricted universe multiverse
# deb http://{ip}:8081/repository/apt-proxy-{ubuntu_version} {ubuntu_version}-backports main restricted universe multiverse
deb-src http://{ip}:8081/repository/apt-proxy-{ubuntu_version} {ubuntu_version} main restricted universe multiverse
deb-src http://{ip}:8081/repository/apt-proxy-{ubuntu_version} {ubuntu_version}-security main restricted universe multiverse
deb-src http://{ip}:8081/repository/apt-proxy-{ubuntu_version} {ubuntu_version}-updates main restricted universe multiverse
# deb-src http://{ip}:8081/repository/apt-proxy-{ubuntu_version} {ubuntu_version}-backports main restricted universe multiverse
"""

ubuntu_apt_arm64 = """
deb http://{ip}:8081/repository/apt-proxy-arm64-{ubuntu_version}  {ubuntu_version} main restricted universe multiverse
deb http://{ip}:8081/repository/apt-proxy-arm64-{ubuntu_version}  {ubuntu_version}-security main restricted universe multiverse
deb http://{ip}:8081/repository/apt-proxy-arm64-{ubuntu_version}  {ubuntu_version}-updates main restricted universe multiverse
# deb http://{ip}:8081/repository/apt-proxy-arm64-{ubuntu_version}  {ubuntu_version}-backports main restricted universe multiverse
deb-src http://{ip}:8081/repository/apt-proxy-arm64-{ubuntu_version}  {ubuntu_version} main restricted universe multiverse
deb-src http://{ip}:8081/repository/apt-proxy-arm64-{ubuntu_version}  {ubuntu_version}-security main restricted universe multiverse
deb-src http://{ip}:8081/repository/apt-proxy-arm64-{ubuntu_version}  {ubuntu_version}-updates main restricted universe multiverse
# deb-src http://{ip}:8081/repository/apt-proxy-arm64-{ubuntu_version}  {ubuntu_version}-backports main restricted universe multiverse
"""


def create_yum_repo():
    if common.get('architectures') == "arm64":
        try:
            if common.get('plat_form') == "ubuntu":
                a_repo = open("/etc/apt/sources.list", "w")
                ip = common.get('local_hostname')
                ubuntu_version = common.get('ubuntu_version')
                a_repo.write(ubuntu_apt_arm64.format(ip=ip, ubuntu_version=ubuntu_version))
            else:
                a_repo = open("/etc/yum.repos.d/kubeops.repo", "w")
                ip = common.get('local_hostname')
                a_repo.write(kubeops_repo_arm64.format(ip=ip))
        except IOError:
            print("Error: 没有找到文件或读取文件失败")
        else:
            print("kubeops.repo: 写入成功")

    if common.get('architectures') == "amd64":
        try:
            if common.get('plat_form') == "ubuntu":
                ip = common.get('local_hostname')
                k_repo = open("/etc/apt/sources.list", "w")
                ubuntu_version = common.get('ubuntu_version')
                k_repo.write(ubuntu_apt_amd64.format(ip=ip, ubuntu_version=ubuntu_version))
            else:
                ip = common.get('local_hostname')
                k_repo = open("/etc/yum.repos.d/kubeops.repo", "w")
                k_repo.write(kubeops_repo_amd64.format(ip=ip))
        except IOError:
            print("Error: 没有找到文件或读取文件失败")
        else:
            print("kubeops.repo: 写入成功")
            k_repo.close()
    if common.get('plat_form') == "centos":
        separate("CentOS", 'yum makecache |', common.get('architectures'))
        cmd = 'yum clean all && rm -rf /var/cache/yum/* && yum makecache'
        system(cmd)
    elif common.get('plat_form') == "ubuntu":
        separate("Ubuntu", 'apt update |', common.get('architectures'))

def separate(v, n, t):
    print("********************", v, n, t, "********************", flush=True)


def raw_download(k8s_version):
    separate(k8s_version, 'Raw downalod |', common.get('architectures'))
    for name, value in raw.raw_url.items():
        url = value
        k = dict()
        k.update(version.version_mg(k8s_version))
        k.update(common)
        v = {
            'k8s_version': k8s_version
        }
        k.update(v)
        url = url.format(**k)
        cmd = 'wget --timeout=600 -nv --no-check-certificate ' + url + ' -P ' + raw_save_dirname
        print('Command: ', cmd)
        system(cmd)
    print('\n')


def rpm_download():
    separate('Ubuntu', 'Rpm download |', common.get('architectures'))
    if common.get('plat_form') == "centos":
        for rpm in rpms.centos_rpms_base:
            cmd = 'yumdownloader --resolve --destdir=' + rpm_save_dirname + ' ' + rpm
            print('Command: ', cmd)
            system(cmd)

    if common.get('plat_form') == "ubuntu":
        for rpm in rpms.deb_base:
            # cmd = 'apt-get install -y --download-only -o=dir::cache=' + rpm_save_dirname + ' ' + rpm
            cmd = 'apt-get install -y ' + rpm
            print('Command: ', cmd)
            system(cmd)
            print('\n')


def image_download(k8s_version):
    try:
        clear_image = "docker system prune --all --volumes -f"
        system(clear_image)
    except SystemError:
        print("Error: 镜像清理失败")

    separate(k8s_version, 'K8S image pull |', common.get('architectures'))
    for name, value in images.k8s_images.items():
        url = value
        k = dict()
        k.update(version.version_mg(k8s_version))
        k.update(common)
        url = url.format(**k)
        cmd_pull = 'docker pull ' + url
        print('Command: ', cmd_pull)
        cmd_remove = 'docker rmi -f ' + url
        system(cmd_pull)
        system(cmd_remove)
    print('\n')

    separate(k8s_version, 'App image pull |', common.get('architectures'))
    for i in range(len(images.app_images)):
        k = dict()
        k.update(common)
        k.update(version.version_mg(k8s_version))
        m = images.app_images[i]
        for image in m:
            img = image.format(**k)
            cmd_pull = 'docker pull ' + img
            print('Command: ', cmd_pull)
            cmd_remove = 'docker rmi -f ' + img
            system(cmd_pull)
            system(cmd_remove)
            print('\n')

    separate(k8s_version, 'Storage image pull |', common.get('architectures'))
    for name, value in images.storage_images.items():
        url = value
        k = dict()
        k.update(version.version_mg(k8s_version))
        k.update(common)
        url = url.format(**k)
        cmd_pull = 'docker pull ' + url
        print('Command: ', cmd_pull)
        cmd_remove = 'docker rmi -f ' + url
        system(cmd_pull)
        system(cmd_remove)
    print('\n')
    separate(k8s_version, 'Download finished |', common.get('architectures'))


def run():
    create_yum_repo()
    kube_version = common.get('kube_version').split(",")
    for i in kube_version:
        if common.get('plat_form') != "ubuntu":
            raw_download(i)
            image_download(i)
    rpm_download()
