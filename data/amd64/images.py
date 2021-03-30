#!/usr/bin/env python3
# coding: utf-8

k8s_images = {
    # Pod image 地址
    'coredns_image_name': '{local_hostname}:{registry_port}/coredns/coredns:{coredns_version}',
    # 基础容器 image 地址
    'sandbox_image': '{local_hostname}:{registry_port}/kubeoperator/pause:{pause_version}-{architectures}',
    # calico 相关镜像
    'calico_typha_image': '{local_hostname}:{registry_port}/calico/typha:{calico_version}-{architectures}',
    'calico_cni_image': '{local_hostname}:{registry_port}/calico/cni:{calico_version}-{architectures}',
    'calico_node_image': '{local_hostname}:{registry_port}/calico/node:{calico_version}-{architectures}',
    'calico_kube_controllers_image': '{local_hostname}:{registry_port}/calico/kube-controllers:{calico_version}-{architectures}',
    'calico_pod2daemon_flexvol_image': '{local_hostname}:{registry_port}/calico/pod2daemon-flexvol:{calico_version}-{architectures}',
    'calicoctl_image': '{local_hostname}:{registry_port}/calico/ctl:{calico_version}-{architectures}',
    # ingress-controller 镜像地址
    'nginx_ingress_image': '{local_hostname}:{registry_port}/kubernetes-ingress-controller/nginx-ingress-controller:{nginx_ingress_version}',
    # metrics-server image
    'metrics_server_image': '{local_hostname}:{registry_port}/kubeoperator/metrics-server:{metrics_server_version}-{architectures}'
}

app_images = {
    # chartmuseum version: 2.13.0, appVersion: 0.12.0
    'chartmuseum_image': '{local_hostname}:{registry_port}/chartmuseum/chartmuseum:v0.12.0',
    # registry version: 1.9.3, appVersion: 2.7.1
    'docker_registry_image': '{local_hostname}:{registry_port}/kubeoperator/registry:2.7.1-amd64'
}
