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
    'calicoctl_download_url': 'http://{local_hostname}:{repo_port}/repository/oss-proxy/calicoctl/{calico_version}/calicoctl-linux-{architectures}',
    # ----------------------- 离线镜像文件下载地址 ----------------------
    'kube_controller_manager_download_url': 'http://{local_hostname}:{repo_port}/repository/oss-proxy/k8s/{k8s_version}/{architectures}/kube-controller-manager.tar',
    'kube_apiserver_download_url': 'http://{local_hostname}:{repo_port}/repository/oss-proxy/k8s/{k8s_version}/{architectures}/kube-apiserver.tar',
    'kube_scheduler_download_url': 'http://{local_hostname}:{repo_port}/repository/oss-proxy/k8s/{k8s_version}/{architectures}/kube-scheduler.tar',
    'kube_proxy_download_url': 'http://{local_hostname}:{repo_port}/repository/oss-proxy/k8s/{k8s_version}/{architectures}/kube-proxy.tar',
    'pause_download_url': 'http://{local_hostname}:{repo_port}/repository/oss-proxy/k8s/{k8s_version}/{architectures}/pause.tar',
    # ----------------------- 存储所需二进制文件下载地址 --------------------
    'govc_download_url': 'http://{local_hostname}:{repo_port}/repository/oss-proxy/govc/{govc_version}/{architectures}/govc_linux_{architectures}.gz',
    'huawei_csi_passwdencrypt_download_url': 'http://{local_hostname}:{repo_port}/repository/oss-proxy/oceanstor/{architectures}/passwdEncrypt',
    # ----------------------- helm 仓库地址 --------------------
    'helm2_download_url': 'http://{local_hostname}:{repo_port}/repository/oss-proxy/helm/{helm_v2_version}/helm-{helm_v2_version}-linux-{architectures}.tar.gz',
    'helm3_download_url': 'http://{local_hostname}:{repo_port}/repository/oss-proxy/helm/{helm_v3_version}/helm-{helm_v3_version}-linux-{architectures}.tar.gz',
    # ----------------------- Openstack VSphere 镜像下载地址 --------------------
    #'openstack_image_download_url': 'http://{local_hostname}:{repo_port}/repository/oss-proxy/terraform/images/openstack/kubeoperator_centos_7.6.1810-1.qcow2',
    #'vsphere_vmdk_download_url': 'http://{local_hostname}:{repo_port}/repository/oss-proxy/terraform/images/vsphere/kubeoperator_centos_7.6.1810/kubeoperator_centos_7.6.1810-1.vmdk',
    #'vsphere_ovf_download_url': 'http://{local_hostname}:{repo_port}/repository/oss-proxy/terraform/images/vsphere/kubeoperator_centos_7.6.1810/kubeoperator_centos_7.6.1810.ovf',
    #'fusioncompute_vhd_download_url': 'http://{local_hostname}:{repo_port}/repository/oss-proxy/terraform/images/fusioncompute/kubeoperator_centos_7.6.1810/kubeoperator_centos_7.6.1810-vda.vhd',
    #'fusioncompute_ovf_download_url': 'http://{local_hostname}:{repo_port}/repository/oss-proxy/terraform/images/fusioncompute/kubeoperator_centos_7.6.1810/kubeoperator_centos_7.6.1810.ovf',
    # ----------------------- Ubuntu chrony 安装包下载地址 --------------------
    'chrony_download_url': "http://{local_hostname}:{repo_port}/repository/oss-proxy/chrony/{architectures}/chrony_xenial.tar.gz"
}