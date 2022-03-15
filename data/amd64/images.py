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
    # cilium image 地址
    'cilium_image': '{local_hostname}:{registry_port}/cilium/cilium:{cilium_version}',
    'cilium_operator_image': '{local_hostname}:{registry_port}/cilium/operator-generic:{cilium_version}',
    # ingress-controller 镜像地址
    'nginx_ingress_image': '{local_hostname}:{registry_port}/kubernetes-ingress-controller/nginx-ingress-controller:{nginx_ingress_version}',
    'traefik_ingress_image': '{local_hostname}:{registry_port}/traefik:{traefik_ingress_version}',
    # metrics-server image
    'metrics_server_image': '{local_hostname}:{registry_port}/kubeoperator/metrics-server:{metrics_server_version}',
    # npd image 地址
    'npd_image': '{local_hostname}:{registry_port}/kubeoperator/node-problem-detector:{npd_version}',
    # kube-bench image
    'kube_bench': '{local_hostname}:{registry_port}/kubeoperator/kube-bench:{kube_bench_version}',
    # helm2 tiller image
    'helm_tiller_image': '{local_hostname}:{registry_port}/kubeoperator/tiller:{helm_v2_version}'
}

app_images = [{
    # kubeapps version: 5.0.1, appVersion: 2.0.1
    '{local_hostname}:{registry_port}/bitnami/kubeapps-apprepository-controller:2.0.1-scratch-r0',
    '{local_hostname}:{registry_port}/bitnami/kubeapps-assetsvc:2.0.1-scratch-r0',
    '{local_hostname}:{registry_port}/bitnami/kubeapps-dashboard:2.0.1-debian-10-r50',
    '{local_hostname}:{registry_port}/bitnami/nginx:1.19.6-debian-10-r18',
    '{local_hostname}:{registry_port}/bitnami/kubeapps-kubeops:2.0.1-scratch-r2',
    '{local_hostname}:{registry_port}/bitnami/postgresql:11.10.0-debian-10-r24',
    '{local_hostname}:{registry_port}/bitnami/kubeapps-asset-syncer:2.0.1-scratch-r0',
    # chartmuseum version: 2.13.0, appVersion: 0.12.0
    '{local_hostname}:{registry_port}/kubeoperator/chartmuseum:v0.12.0',
    # registry version: 1.9.3, appVersion: 2.7.1
    '{local_hostname}:{registry_port}/kubeoperator/registry:2.7.1',
    # efk version: 1.0.0,appVersion: 7.6.2
    '{local_hostname}:{registry_port}/fluentd_elasticsearch/fluentd:v2.8.0',
    '{local_hostname}:{registry_port}/elasticsearch/elasticsearch:7.6.2',
    # promethus version: 11.5.0 , appVersion: v2.20.1
    '{local_hostname}:{registry_port}/prom/node-exporter:v1.0.1',
    '{local_hostname}:{registry_port}/carlosedp/kube-state-metrics:v1.9.5',
    '{local_hostname}:{registry_port}/jimmidyson/configmap-reload:v0.4.0',
    '{local_hostname}:{registry_port}/prom/prometheus:v2.20.1',
    # f5
    '{local_hostname}:{registry_port}/kubeoperator/k8s-bigip-ctlr:1.9.2-amd64',
    # loki
    '{local_hostname}:{registry_port}/grafana/loki:2.0.0',
    '{local_hostname}:{registry_port}/grafana/promtail:2.0.0',
    # istio
    '{local_hostname}:{registry_port}/istio/pilot:{istio_version}',
    '{local_hostname}:{registry_port}/istio/proxyv2:{istio_version}',
    # grafana
    '{local_hostname}:{registry_port}/grafana/grafana:7.3.3',
    '{local_hostname}:{registry_port}/curlimages/curl:7.73.0',
    '{local_hostname}:{registry_port}/kubeoperator/busybox:{busybox_version}',
    # opa gatekeeper
    '{local_hostname}:{registry_port}/openpolicyagent/gatekeeper:{gatekeeper_version}',
    '{local_hostname}:{registry_port}/openpolicyagent/gatekeeper-crds:{gatekeeper_version}',
    # velero
    '{local_hostname}:{registry_port}/velero/velero:v1.7.1',
    '{local_hostname}:{registry_port}/velero/velero-plugin-for-aws:v1.2.1',
    '{local_hostname}:{registry_port}/kubeoperator/velero:1.4.2-2b9dce65-aliyun',
    '{local_hostname}:{registry_port}/kubeoperator/velero-plugin-alibabacloud:v1.0.0-2d33b89'
},
    {
        # kubeapps
        '{local_hostname}:{registry_port}/bitnami/kubeapps-asset-syncer:2.4.2-scratch-r0',
        '{local_hostname}:{registry_port}/bitnami/nginx:1.21.4-debian-10-r26',
        '{local_hostname}:{registry_port}/bitnami/kubeapps-apprepository-controller:2.4.2-scratch-r0',
        '{local_hostname}:{registry_port}/bitnami/kubeapps-dashboard:2.4.2-debian-10-r0',
        '{local_hostname}:{registry_port}/bitnami/kubeapps-apis:2.4.2-debian-10-r1',
        '{local_hostname}:{registry_port}/bitnami/kubeapps-kubeops:2.4.2-scratch-r0',
        '{local_hostname}:{registry_port}/bitnami/postgresql:11.14.0-debian-10-r0',
        # loki version: 2.0.0 , appVersion: v2.0.0
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
    # ceph-rbd provisioner
    'rbd_provisioner_image': '{local_hostname}:{registry_port}/external_storage/rbd-provisioner:{rbd_provisioner_version}',
    # nfs provisioner
    'nfs_client_provisioner_image': '{local_hostname}:{registry_port}/kubeoperator/nfs-client-provisioner:{nfs_provisioner_version}',
    # rook ceph
    'ceph_image': '{local_hostname}:{registry_port}/ceph/ceph:{ceph_version}',
    'rook_ceph_image': '{local_hostname}:{registry_port}/rook/ceph:{rook_ceph_version}',
    'rook_csi_ceph_image': '{local_hostname}:{registry_port}/cephcsi/cephcsi:{rook_csi_ceph_version}',
    'rook_csi_registrar_image': '{local_hostname}:{registry_port}/k8scsi/csi-node-driver-registrar:{rook_csi_node_driver_registrar_version}',
    'rook_csi_resizer_image': '{local_hostname}:{registry_port}/k8scsi/csi-resizer:{rook_csi_resizer_version}',
    'rook_csi_provisioner_image': '{local_hostname}:{registry_port}/k8scsi/csi-provisioner:{rook_csi_provisioner_version}',
    'rook_csi_snapshotter_image': '{local_hostname}:{registry_port}/k8scsi/csi-snapshotter:{rook_csi_snapshotter_version}',
    'rook_csi_attacher_image': '{local_hostname}:{registry_port}/k8scsi/csi-attacher:{rook_csi_attacher_version}',
    # oceanstor csi
    'huawei_csi_driver_image': '{local_hostname}:{registry_port}/kubeoperator/huawei-csi:{huawei_csi_driver_version}',
    'huawei_csi_provisioner_image': '{local_hostname}:{registry_port}/k8scsi/csi-provisioner:{huawei_csi_provisioner_version}',
    'huawei_csi_attacher_image': '{local_hostname}:{registry_port}/k8scsi/csi-attacher:{huawei_csi_attacher_version}',
    'huawei_csi_node_driver_registrar_image': '{local_hostname}:{registry_port}/k8scsi/csi-node-driver-registrar:{huawei_csi_node_driver_registrar_version}',
    # vsphere csi
    'vsphere_csi_driver_image': '{local_hostname}:{registry_port}/kubeoperator/vsphere-csi-driver:{vsphere_csi_version}',
    'vsphere_csi_syncer_image': '{local_hostname}:{registry_port}/kubeoperator/vsphere-csi-syncer:{vsphere_csi_version}',
    'vsphere_csi_livenessprobe_image': '{local_hostname}:{registry_port}/k8scsi/livenessprobe:{vsphere_csi_livenessprobe_version}',
    'vsphere_csi_provisioner_image': '{local_hostname}:{registry_port}/k8scsi/csi-provisioner:{vsphere_csi_provisioner_version}',
    'vsphere_csi_attacher_image': '{local_hostname}:{registry_port}/k8scsi/csi-attacher:{vsphere_csi_attacher_version}',
    'vsphere_csi_node_driver_registrar_image': '{local_hostname}:{registry_port}/k8scsi/csi-node-driver-registrar:{vsphere_csi_node_driver_registrar_version}',
    # cinder csi
    'cinder_csi_driver_image': '{local_hostname}:{registry_port}/k8scloudprovider/cinder-csi-plugin:{cinder_csi_version}',
    'cinder_csi_attacher_image': '{local_hostname}:{registry_port}/k8scsi/csi-attacher:{cinder_csi_attacher_version}',
    'cinder_csi_provisioner_image': '{local_hostname}:{registry_port}/k8scsi/csi-provisioner:{cinder_csi_provisioner_version}',
    'cinder_csi_snapshotter_image': '{local_hostname}:{registry_port}/k8scsi/csi-snapshotter:{cinder_csi_snapshotter_version}',
    'cinder_csi_resizer_image': '{local_hostname}:{registry_port}/k8scsi/csi-resizer:{cinder_csi_resizer_version}',
    'cinder_csi_livenessprobe_image': '{local_hostname}:{registry_port}/k8scsi/livenessprobe:{cinder_csi_livenessprobe_version}',
    'cinder_csi_registrar_image': '{local_hostname}:{registry_port}/k8scsi/csi-node-driver-registrar:{cinder_csi_node_driver_registrar_version}'
}
