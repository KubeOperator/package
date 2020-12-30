import socket,platform,sys
from os import system,mkdir,getcwd


# 获取系统平台架构
def get_host_arch():
    ar = platform.uname().machine
    if ar == 'x86_64':
        os = "amd64"
    elif ar == 'aarch64':
        os = 'arm64'
    return os


if get_host_arch() == 'amd64':
    from requirements.amd64 import images, raw, rpms, version
elif get_host_arch() == 'arm64':
    from requirements.arm64 import images, raw, rpms, version



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

# kubernetes 版本管理
def version_mg(vs):
    v = {
        'v1.18.6' : version.v1_18_4,
        'v1.18.8' : version.v1_18_6,
    }

    return v.get(vs,"没有数据")

# 下载
def download_images(kube_version):
        for name, value in images.images.items():
            url = value
            k = dict()
            k.update(version_mg(kube_version))
            k.update(common)
            url = url.format(**k)
            cmd_pull = 'echo docker pull '+url
            cmd_remove = 'echo docker rmi -f '+url
            system(cmd_pull)
            system(cmd_remove)

        for name, value in raw.raw_url.items():
            url = value
            k = dict()
            k.update(version_mg(kube_version))
            k.update(common)
            url = url.format(**k)
            cmd = 'wget --timeout=600 --no-check-certificate ' + url + ' -p '+ raw_save_dirname
            print(cmd)

        for name in rpms.rpms_base:
            cmd = 'yumdownloader --resolve --destdir=' + rpms_save_dirname + ' ' + name
            print(cmd)
            # system(cmd)


def run():
    kube_version = common.get('kube_version')
    download_images(kube_version)
