#!/usr/bin/env python3
# coding: utf-8

k8s_images = {
    # Pod image 地址
    'coredns_image_name': '{local_hostname}:{registry_port}/coredns/coredns:{coredns_version}',
    # pod_infra_container_image: 'k8s.gcr.io/pause:{pause_version}'
    # 基础容器 image 地址
    'sandbox_image': '{local_hostname}:{registry_port}/kubeoperator/pause:{pause_version}-{architectures}',
    # busybox_image image 地址
    'busybox_image': '{local_hostname}:{registry_port}/kubeoperator/busybox:{busybox_version}-{architectures}',
    # calico 相关镜像
    'calico_typha_image': '{local_hostname}:{registry_port}/calico/typha:{calico_version}-{architectures}',
    'calico_cni_image': '{local_hostname}:{registry_port}/calico/cni:{calico_version}-{architectures}',
    'calico_node_image': '{local_hostname}:{registry_port}/calico/node:{calico_version}-{architectures}',
    'calico_kube_controllers_image': '{local_hostname}:{registry_port}/calico/kube-controllers:{calico_version}-{architectures}',
    'calico_pod2daemon_flexvol_image': '{local_hostname}:{registry_port}/calico/pod2daemon-flexvol:{calico_version}-{architectures}',
    'calicoctl_image': '{local_hostname}:{registry_port}/calico/ctl:{calico_version}-{architectures}',
    # flannel image 地址
    'flannel_image': '{local_hostname}:{registry_port}/coreos/flannel:{flannel_version}-{architectures}',
    # ingress-controller 镜像地址
    'nginx_ingress_image': '{local_hostname}:{registry_port}/kubernetes-ingress-controller/nginx-ingress-controller:{nginx_ingress_version}',
    'traefik_ingress_image': '{local_hostname}:{registry_port}/traefik:{traefik_ingress_version}',
    # ceph-rbd provisioner
    'rbd_provisioner_image': '{local_hostname}:{registry_port}/external_storage/rbd-provisioner:{rbd_provisioner_version}',
    # nfs provisioner
    'nfs_client_provisioner_image': '{local_hostname}:{registry_port}/kubeoperator/nfs-client-provisioner:{nfs_provisioner_version}-{architectures}',
    # metrics-server image
    'metrics_server_image': '{local_hostname}:{registry_port}/kubeoperator/metrics-server:{metrics_server_version}-{architectures}',
    # npd image 地址
    'npd_image': '{local_hostname}:{registry_port}/kubeoperator/node-problem-detector:{npd_versioon}-{architectures}',
    # kube-bench image
    'kube_bench': '{local_hostname}:{registry_port}/kubeoperator/kube-bench:{kube_bench_version}-{architectures}'
}

app_images = {
    # registry
    '{local_hostname}:{registry_port}/kubeoperator/registry:2.7.1-arm64',
    # dashboard
    '{local_hostname}:{registry_port}/kubernetesui/dashboard:v2.0.3',
    '{local_hostname}:{registry_port}/kubernetesui/metrics-scraper:v1.0.4',
    # prometheus
    '{local_hostname}:{registry_port}/prom/node-exporter:v0.18.1',
    '{local_hostname}:{registry_port}/carlosedp/kube-state-metrics:v1.9.5',
    '{local_hostname}:{registry_port}/prom/alertmanager:v0.20.0',
    '{local_hostname}:{registry_port}/jimmidyson/configmap-reload:v0.3.0',
    '{local_hostname}:{registry_port}/prom/pushgateway:v1.0.1',
    '{local_hostname}:{registry_port}/prom/prometheus:v2.18.1',
    # loki
    '{local_hostname}:{registry_port}/grafana/loki:2.0.0-arm64',
    '{local_hostname}:{registry_port}/grafana/promtail:2.0.0-arm64',
    # chartmuseum
    '{local_hostname}:{registry_port}/kubeoperator/chartmuseum:v0.12.0-arm64',
    # grafana
    '{local_hostname}:{registry_port}/kubeoperator/grafana:7.3.3-arm64'
}