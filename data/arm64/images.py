#!/usr/bin/env python3
# coding: utf-8

k8s_images = {
    # Pod image 地址
    'coredns_image_name': '{local_hostname}:{registry_port}/coredns/coredns:{coredns_version}',
    # dns cache image 地址
    'dns_cache_image': '{local_hostname}:{registry_port}/kubeoperator/k8s-dns-node-cache:{dns_cache_version}',
    # 基础容器 image 地址
    'sandbox_image': '{local_hostname}:{registry_port}/kubeoperator/pause:{pause_version}',
    # busybox_image image 地址
    'busybox_image': '{local_hostname}:{registry_port}/kubeoperator/busybox:{busybox_version}',
    # calico 相关镜像
    'calico_typha_image': '{local_hostname}:{registry_port}/calico/typha:{calico_version}',
    'calico_cni_image': '{local_hostname}:{registry_port}/calico/cni:{calico_version}',
    'calico_node_image': '{local_hostname}:{registry_port}/calico/node:{calico_version}',
    'calico_kube_controllers_image': '{local_hostname}:{registry_port}/calico/kube-controllers:{calico_version}',
    'calico_pod2daemon_flexvol_image': '{local_hostname}:{registry_port}/calico/pod2daemon-flexvol:{calico_version}',
    'calicoctl_image': '{local_hostname}:{registry_port}/calico/ctl:{calico_version}',
    # flannel image 地址
    'flannel_image': '{local_hostname}:{registry_port}/coreos/flannel:{flannel_version}',
    # ingress-controller 镜像地址
    'nginx_ingress_image': '{local_hostname}:{registry_port}/kubernetes-ingress-controller/nginx-ingress-controller:{nginx_ingress_version}',
    'traefik_ingress_image': '{local_hostname}:{registry_port}/traefik:{traefik_ingress_version}',
    # metrics-server image
    'metrics_server_image': '{local_hostname}:{registry_port}/kubeoperator/metrics-server:{metrics_server_version}',
    # npd image 地址
    'npd_image': '{local_hostname}:{registry_port}/kubeoperator/node-problem-detector:{npd_version}',
    # kube-bench image
    'kube_bench': '{local_hostname}:{registry_port}/kubeoperator/kube-bench:{kube_bench_version}'
}

app_images = [{
    # registry
    '{local_hostname}:{registry_port}/kubeoperator/registry:2.7.1',
    # promethus
    '{local_hostname}:{registry_port}/prom/node-exporter:v1.0.1',
    '{local_hostname}:{registry_port}/carlosedp/kube-state-metrics:v1.9.5',
    '{local_hostname}:{registry_port}/jimmidyson/configmap-reload:v0.4.0',
    '{local_hostname}:{registry_port}/prom/prometheus:v2.20.1',
    # loki
    '{local_hostname}:{registry_port}/grafana/loki:2.0.0',
    '{local_hostname}:{registry_port}/grafana/promtail:2.0.0',
    # chartmuseum
    '{local_hostname}:{registry_port}/kubeoperator/chartmuseum:v0.12.0',
    # grafana
    '{local_hostname}:{registry_port}/grafana/grafana:7.3.3',
    '{local_hostname}:{registry_port}/curlimages/curl:7.73.0',
    '{local_hostname}:{registry_port}/kubeoperator/busybox:{busybox_version}',
    # opa gatekeeper
    '{local_hostname}:{registry_port}/openpolicyagent/gatekeeper:{gatekeeper_version}',
    '{local_hostname}:{registry_port}/openpolicyagent/gatekeeper-crds:{gatekeeper_version}',
    # velero
    '{local_hostname}:{registry_port}/velero/velero:v1.7.1',
    '{local_hostname}:{registry_port}/velero/velero-plugin-for-aws:v1.2.1'
},
    {
        # loki
        '{local_hostname}:{registry_port}/grafana/promtail:2.1.0',
        '{local_hostname}:{registry_port}/grafana/loki:2.1.0',
        # promethus
        '{local_hostname}:{registry_port}/dyrnq/kube-state-metrics:v2.2.4',
        '{local_hostname}:{registry_port}/prometheus/node-exporter:v1.3.0',
        '{local_hostname}:{registry_port}/jimmidyson/configmap-reload:v0.5.0',
        '{local_hostname}:{registry_port}/prometheus/prometheus:v2.31.1',
        # grafana
        '{local_hostname}:{registry_port}/grafana/grafana:8.3.1',
        '{local_hostname}:{registry_port}/curlimages/curl:7.73.0',
        '{local_hostname}:{registry_port}/kubeoperator/busybox:1.31.1'
    }
]

storage_images = {
    # nfs provisioner
    'nfs_client_provisioner_image': '{local_hostname}:{registry_port}/kubeoperator/nfs-client-provisioner:{nfs_provisioner_version}'
}
