#!/usr/bin/env python3
# coding: utf-8

k8s_images = {
    # coredns
    'coredns_image_name': '{local_hostname}:{registry_port}/coredns/coredns:{coredns_version}',
    # dns cache
    'dns_cache_image': '{local_hostname}:{registry_port}/kubeoperator/k8s-dns-node-cache:{dns_cache_version}',
    # sandbox
    'sandbox_image': '{local_hostname}:{registry_port}/kubeoperator/pause:{pause_version}',
    # busybox
    'busybox_image': '{local_hostname}:{registry_port}/kubeoperator/busybox:{busybox_version}',
    # calico
    'calico_typha_image': '{local_hostname}:{registry_port}/calico/typha:{calico_version}',
    'calico_cni_image': '{local_hostname}:{registry_port}/calico/cni:{calico_version}',
    'calico_node_image': '{local_hostname}:{registry_port}/calico/node:{calico_version}',
    'calico_kube_controllers_image': '{local_hostname}:{registry_port}/calico/kube-controllers:{calico_version}',
    'calico_pod2daemon_flexvol_image': '{local_hostname}:{registry_port}/calico/pod2daemon-flexvol:{calico_version}',
    'calicoctl_image': '{local_hostname}:{registry_port}/calico/ctl:{calico_version}',
    # flannel
    'flannel_image': '{local_hostname}:{registry_port}/coreos/flannel:{flannel_version}',
    # ingress-controller
    'nginx_ingress_image': '{local_hostname}:{registry_port}/kubeoperator/ingress-nginx-controller:{nginx_ingress_version}',
    'traefik_ingress_image': '{local_hostname}:{registry_port}/traefik:{traefik_ingress_version}',
    # metrics-server
    'metrics_server_image': '{local_hostname}:{registry_port}/kubeoperator/metrics-server:{metrics_server_version}',
    # npd
    'npd_image': '{local_hostname}:{registry_port}/kubeoperator/node-problem-detector:{npd_version}',
    # kube-bench
    'kube_bench': '{local_hostname}:{registry_port}/kubeoperator/kube-bench:{kube_bench_version}'
}

app_images = [{
    # registry
    '{local_hostname}:{registry_port}/kubeoperator/registry:2.7.1',
    # promethus
    '{local_hostname}:{registry_port}/dyrnq/kube-state-metrics:v2.4.1',
    '{local_hostname}:{registry_port}/prometheus/node-exporter:v1.3.0',
    '{local_hostname}:{registry_port}/jimmidyson/configmap-reload:v0.5.0',
    '{local_hostname}:{registry_port}/prometheus/prometheus:v2.34.0',
    # loki
    '{local_hostname}:{registry_port}/grafana/promtail:2.1.0',
    '{local_hostname}:{registry_port}/grafana/loki:2.1.0',
    # chartmuseum
    '{local_hostname}:{registry_port}/kubeoperator/chartmuseum:v0.12.0',
    # grafana
    '{local_hostname}:{registry_port}/grafana/grafana:8.3.1',
    '{local_hostname}:{registry_port}/curlimages/curl:7.73.0',
    '{local_hostname}:{registry_port}/kubeoperator/busybox:1.31.1',
    # opa gatekeeper
    '{local_hostname}:{registry_port}/openpolicyagent/gatekeeper:{gatekeeper_version}',
    '{local_hostname}:{registry_port}/openpolicyagent/gatekeeper-crds:{gatekeeper_version}',
    # metallb
    '{local_hostname}:{registry_port}/metallb/controller:{metallb_version}',
    '{local_hostname}:{registry_port}/metallb/speaker:{metallb_version}',
    # velero
    '{local_hostname}:{registry_port}/velero/velero:v1.7.1',
    '{local_hostname}:{registry_port}/velero/velero-plugin-for-aws:v1.2.1'
}]

storage_images = {
    # nfs provisioner
    'nfs_client_provisioner_image': '{local_hostname}:{registry_port}/kubeoperator/nfs-client-provisioner:{nfs_provisioner_version}'
}
