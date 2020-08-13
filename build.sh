#!/usr/bin/env bash
CURRENT_DIR=$(
   cd "$(dirname "$0")"
   pwd
)

os=`uname -a`

# 判断系统架构
if [[ $os =~ 'x86_64' ]];then
  architectures=amd64
  ansible_architecture=x86_64
elif [[ $os =~ 'aarch64' ]];then
  architectures=arm64
  ansible_architecture=aarch64
else
  architectures=amd64
  ansible_architecture=x86_64
fi

source ./requirements/tag_list
source ./requirements/images_list
source ./requirements/raw_list
source ./requirements/rpms_list

function prapre_dir() {
  mkdir -p $CURRENT_DIR/{raw,images,rpms}
  raw_save_dirname=$CURRENT_DIR/raw
  rpms_save_dirname=$CURRENT_DIR/rpms
  images_save_dirname=$CURRENT_DIR/images
}

function download_image() {
echo "+++++++++++++++++++++++++++++++++++下载 Docker 镜像++++++++++++++++++++++++++++++++++++++++++++++++++++++"
  for image in ${K8S_IMAGES[@]}
    do
      image_name=`echo $image|awk -F= '{print $1}'`
      echo "下载 ${image_name} >>"
      docker pull `echo ${image}|awk -F= '{print $2}'`
      docker rmi `echo $image|awk -F= '{print $2}'`
    done
  if [ ${architectures} = "amd64" ];then
  for image in ${APPLICATION_IMAGES_AMD64[@]}
    do
      echo "AMD | 下载 ${image} >>"
      docker pull ${image}
      docker rmi ${image}
    done
  elif [ ${architectures} = "arm64" ]; then
  for image in ${APPLICATION_IMAGES_ARM64[@]}
    do
      echo "ARM | 下载 ${image} >>"
      docker pull ${image}
      docker rmi ${image}
    done
  fi
}

function download_raw() {
echo "+++++++++++++++++++++++++++++++++++下载 二进制文件++++++++++++++++++++++++++++++++++++++++++++++++++++++"

  for raw in ${RAW[@]}
  do
    raw_name=`echo $raw|awk -F= '{print $1}'`
    echo "下载 ${raw_name} >>"
    wget --timeout=${wget_timeout} -nv `echo $raw|awk -F= '{print $2}'` -P ${raw_save_dirname}
  done
}

function download_rpm() {
echo "+++++++++++++++++++++++++++++++++++下载 rpm ++++++++++++++++++++++++++++++++++++++++++++++++++++++"
  yum clean all && yum makecache
  for rpm in ${RPMS[@]}
  do
    rpm_name=`echo $rpm|awk -F= '{print $1}'`
    echo "下载 ${rpm_name} >>"
    yumdownloader --resolve --destdir=${rpms_save_dirname}  `echo $rpm|awk -F= '{print $1}'`
  done
}

function main() {
  prapre_dir
  download_image
  download_raw
  download_rpm
}

main
