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
    'kube_bench': '{local_hostname}:{registry_port}/kubeoperator/kube-bench:{kube_bench_version}-{architectures}',
    # helm2 tiller image
    'helm_tiller_image': '{local_hostname}:{registry_port}/kubeoperator/tiller:{helm_v2_version}'
}

app_images = [{
    # kubeapps version: 3.7.2,appVersion: v1.10.2
    '{local_hostname}:{registry_port}/bitnami/nginx:1.18.0-debian-10-r38',
    '{local_hostname}:{registry_port}/bitnami/kubeapps-apprepository-controller:1.10.2-scratch-r0',
    '{local_hostname}:{registry_port}/bitnami/kubeapps-assetsvc:1.10.2-scratch-r0',
    '{local_hostname}:{registry_port}/bitnami/kubeapps-dashboard:1.10.2-debian-10-r0',
    '{local_hostname}:{registry_port}/bitnami/kubeapps-tiller-proxy:1.10.2-scratch-r0',
    '{local_hostname}:{registry_port}/postgres:11-alpine',
    '{local_hostname}:{registry_port}/bitnami/kubeapps-asset-syncer:1.10.2-scratch-r0',
    '{local_hostname}:{registry_port}/bitnami/kubectl:1.16.3-debian-10-r85',
    '{local_hostname}:{registry_port}/bitnami/kubeapps-kubeops:1.10.2-scratch-r0',
    # chartmuseum version: 2.13.0, appVersion: 0.12.0
    '{local_hostname}:{registry_port}/chartmuseum/chartmuseum:v0.12.0',
    # registry version: 1.9.3, appVersion: 2.7.1
    '{local_hostname}:{registry_port}/kubeoperator/registry:2.7.1-amd64',
    # efk version: 1.0.0,appVersion: 7.6.2
    '{local_hostname}:{registry_port}/fluentd_elasticsearch/fluentd:v2.8.0',
    '{local_hostname}:{registry_port}/elasticsearch/elasticsearch:7.6.2',
    # dashboard version: 2.2.0, appVersion: 2.0.3
    '{local_hostname}:{registry_port}/kubernetesui/dashboard:v2.0.3',
    '{local_hostname}:{registry_port}/kubernetesui/metrics-scraper:v1.0.4',
    # prometheus version: 11.5.0,appVersion: 2.18.1
    '{local_hostname}:{registry_port}/prom/node-exporter:v0.18.1',
    '{local_hostname}:{registry_port}/coreos/kube-state-metrics:v1.9.5',
    '{local_hostname}:{registry_port}/prom/alertmanager:v0.20.0',
    '{local_hostname}:{registry_port}/jimmidyson/configmap-reload:v0.3.0',
    '{local_hostname}:{registry_port}/prom/pushgateway:v1.0.1',
    '{local_hostname}:{registry_port}/prom/prometheus:v2.18.1',
    # rook-ceph
    '{local_hostname}:{registry_port}/ceph/ceph:{ceph_image_version}',
    '{local_hostname}:{registry_port}/cephcsi/cephcsi:{csi_ceph_image_version}',
    '{local_hostname}:{registry_port}/k8scsi/csi-node-driver-registrar:{csi_registrar_image_version}',
    '{local_hostname}:{registry_port}/k8scsi/csi-resizer:{csi_resizer_image_version}',
    '{local_hostname}:{registry_port}/k8scsi/csi-provisioner:{csi_provisioner_image_version}',
    '{local_hostname}:{registry_port}/k8scsi/csi-snapshotter:{csi_snapshotter_image_version}',
    '{local_hostname}:{registry_port}/k8scsi/csi-attacher:{csi_attacher_image_version}',
    # f5
    '{local_hostname}:{registry_port}/kubeoperator/k8s-bigip-ctlr:1.9.2-amd64',
    # oceanstor csi
    '{local_hostname}:{registry_port}/k8scsi/csi-provisioner:v1.4.0',
    '{local_hostname}:{registry_port}/k8scsi/csi-attacher:v1.2.1',
    '{local_hostname}:{registry_port}/k8scsi/csi-node-driver-registrar:v1.2.0',
    '{local_hostname}:{registry_port}/kubeoperator/huawei-csi:2.2.9',
    '{local_hostname}:{registry_port}/nvidia/k8s-device-plugin:1.0.0-beta',
    # loki
    '{local_hostname}:{registry_port}/grafana/loki:2.0.0-amd64',
    '{local_hostname}:{registry_port}/grafana/promtail:2.0.0-amd64',
    # istio
    '{local_hostname}:{registry_port}/istio/pilot:{istio_version}',
    '{local_hostname}:{registry_port}/istio/proxyv2:{istio_version}',
    # grafana
    '{local_hostname}:{registry_port}/kubeoperator/grafana:7.3.3-amd64',
    '{local_hostname}:{registry_port}/curlimages/curl:7.73.0'
},
    {
        # kubeapps version: 5.0.1, appVersion: 2.0.1
        '{local_hostname}:{registry_port}/bitnami/kubeapps-apprepository-controller:2.0.1-scratch-r0',
        '{local_hostname}:{registry_port}/bitnami/kubeapps-assetsvc:2.0.1-scratch-r0',
        '{local_hostname}:{registry_port}/bitnami/kubeapps-dashboard:2.0.1-debian-10-r50',
        '{local_hostname}:{registry_port}/bitnami/nginx:1.19.6-debian-10-r18',
        '{local_hostname}:{registry_port}/bitnami/kubeapps-kubeops:2.0.1-scratch-r2',
        '{local_hostname}:{registry_port}/bitnami/postgresql:11.10.0-debian-10-r24',
        '{local_hostname}:{registry_port}/bitnami/nginx:1.19.6-debian-10-r18',
        '{local_hostname}:{registry_port}/bitnami/kubectl:1.18.14-debian-10-r12',
        '{local_hostname}:{registry_port}/bitnami/kubeapps-asset-syncer:2.0.1-scratch-r0',
        '{local_hostname}:{registry_port}/bitnami/kubectl:1.18.14-debian-10-r12',
        # loki version: 2.0.0 , appVersion: v2.0.0
        '{local_hostname}:{registry_port}/grafana/promtail:2.1.0',
        '{local_hostname}:{registry_port}/grafana/loki:2.1.0',
        '{local_hostname}:{registry_port}/ats/bats:v1.1.0',
        # promethus version: 11.5.0 , appVersion: 2.18.1
        '{local_hostname}:{registry_port}/prom/node-exporter:v1.0.1',
        '{local_hostname}:{registry_port}/coreos/kube-state-metrics:v1.9.5',
        '{local_hostname}:{registry_port}/prom/alertmanager:v0.20.0',
        '{local_hostname}:{registry_port}/jimmidyson/configmap-reload:v0.3.0',
        '{local_hostname}:{registry_port}/prom/pushgateway:v1.0.1',
        '{local_hostname}:{registry_port}/jimmidyson/configmap-reload:v0.4.0',
        '{local_hostname}:{registry_port}/prom/prometheus:v2.20.1'
    }
]
