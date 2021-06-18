#!/usr/bin/env python3
# coding: utf-8

raw_url = {
    # ----------------------- k8s 二进制文件下载地址 --------------------
    'k8s_download_url': 'http://{local_hostname}:{repo_port}/repository/oss-proxy/k8s/{k8s_version}/{architectures}/k8s.tar.gz',
    'etcd_download_url': 'http://{local_hostname}:{repo_port}/repository/oss-proxy/etcd/{etcd_version}/{architectures}/etcd-{etcd_version}-linux-{architectures}.tar.gz',
    'cni_download_url': 'http://{local_hostname}:{repo_port}/repository/oss-proxy/containernetworking/{cni_version}/{architectures}/cni-plugins-linux-{architectures}-{cni_version}.tgz',
    'docker_download_url': 'http://{local_hostname}:{repo_port}/repository/oss-proxy/docker/{docker_version}/{architectures}/docker-{docker_version}.tgz',
    'containerd_download_url': 'http://{local_hostname}:{repo_port}/repository/oss-proxy/containerd/{containerd_version}/{architectures}/containerd-{containerd_version}-linux-{architectures}.tar.gz',
    'crictl_download_url': 'http://{local_hostname}:{repo_port}/repository/oss-proxy/crictl/{crictl_version}/{architectures}/crictl-{crictl_version}-linux-{architectures}.tar.gz',
    'runc_download_url': 'http://{local_hostname}:{repo_port}/repository/oss-proxy/runc/{runc_version}/{architectures}/runc.{architectures}',
    'cni_calico_download_url': 'http://{local_hostname}:{repo_port}/repository/oss-proxy/cni-plugin/{cni_calico_version}/{architectures}/calico-{architectures}',
    'cni_calico_ipam_download_url': 'http://{local_hostname}:{repo_port}/repository/oss-proxy/cni-plugin/{cni_calico_version}/{architectures}/calico-ipam-{architectures}',
    # ----------------------- 离线镜像文件下载地址 ----------------------
    'kube_controller_manager_download_url': 'http://{local_hostname}:{repo_port}/repository/oss-proxy/k8s/{k8s_version}/{architectures}/kube-controller-manager.tar',
    'kube_apiserver_download_url': 'http://{local_hostname}:{repo_port}/repository/oss-proxy/k8s/{k8s_version}/{architectures}/kube-apiserver.tar',
    'kube_scheduler_download_url': 'http://{local_hostname}:{repo_port}/repository/oss-proxy/k8s/{k8s_version}/{architectures}/kube-scheduler.tar',
    'kube_proxy_download_url': 'http://{local_hostname}:{repo_port}/repository/oss-proxy/k8s/{k8s_version}/{architectures}/kube-proxy.tar',
    'pause_download_url': 'http://{local_hostname}:{repo_port}/repository/oss-proxy/k8s/{k8s_version}/{architectures}/pause.tar',
    # ----------------------- helm 仓库地址 --------------------
    'helm3_download_url': 'http://{local_hostname}:{repo_port}/repository/oss-proxy/helm/{helm_v3_version}/helm-{helm_v3_version}-linux-{architectures}.tar.gz',
    # ----------------------- Ubuntu chrony 安装包下载地址 --------------------
    'chrony_download_url': "http://{local_hostname}:{repo_port}/repository/oss-proxy/chrony/{architectures}/chrony_xenial.tar.gz"
}