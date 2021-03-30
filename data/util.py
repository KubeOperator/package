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
images_save_dirname = current_dir+'/images'

try:
    mkdir(raw_save_dirname)
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
    'kube_version': sys.argv[1]
}

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
    for name, value in images.app_images.items():
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

    separate(k8s_version,'Download finished |',common.get('architectures'))

def run():
    kube_version = common.get('kube_version')
    download(kube_version)

