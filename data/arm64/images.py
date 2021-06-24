#!/usr/bin/env python3
# coding: utf-8

k8s_images = {
    # Pod image 地址
    'coredns_image_name': '{local_hostname}:{registry_port}/coredns/coredns:{coredns_version}',
    # 基础容器 image 地址
    'sandbox_image': '{local_hostname}:{registry_port}/kubeoperator/pause:{pause_version}',
    # calico 相关镜像
    'calico_typha_image': '{local_hostname}:{registry_port}/calico/typha:{calico_version}',
    'calico_cni_image': '{local_hostname}:{registry_port}/calico/cni:{calico_version}',
    'calico_node_image': '{local_hostname}:{registry_port}/calico/node:{calico_version}',
    'calico_kube_controllers_image': '{local_hostname}:{registry_port}/calico/kube-controllers:{calico_version}',
    'calico_pod2daemon_flexvol_image': '{local_hostname}:{registry_port}/calico/pod2daemon-flexvol:{calico_version}',
    'calicoctl_image': '{local_hostname}:{registry_port}/calico/ctl:{calico_version}',
    # ingress-controller 镜像地址
    'nginx_ingress_image': '{local_hostname}:{registry_port}/kubernetes-ingress-controller/nginx-ingress-controller:{nginx_ingress_version}',
    # metrics-server image
    'metrics_server_image': '{local_hostname}:{registry_port}/kubeoperator/metrics-server:{metrics_server_version}'
}

app_images = {
    # registry
    'docker_registry_image': '{local_hostname}:{registry_port}/kubeoperator/registry:2.7.1-arm64',
    # chartmuseum
    'chartmuseum_image': '{local_hostname}:{registry_port}/kubeoperator/chartmuseum:v0.12.0-arm64'
}
