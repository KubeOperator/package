#!/usr/bin/env python3
# coding: utf-8

# kubernetes 版本管理
def version_mg(vs):
    v = {
        'v1.18.4': v1_18_4,
        'v1.18.6' : v1_18_6,
        'v1.18.8': v1_18_8,
        'v1.18.10': v1_18_10,
        'v1.18.12': v1_18_12,
        'v1.18.14': v1_18_14,
        'v1.18.15': v1_18_15,
        'v1.20.4': v1_20_4,
    }
    return v.get(vs,'none version')

v1_18_4 =  {
    'pause_version':  '3.2',
    'busybox_version': '1.28',
    'crictl_version': 'v1.18.0',
    'npd_version': 'v0.8.1',
    'kube_bench_version': 'v0.0.1',
    'runc_version': 'v1.0.0-rc91',
    'cni_version': 'v0.8.6',
    'cni_calico_version': 'v3.12.3',
    # 存储类镜像版本设置
    'rbd_provisioner_version': 'v2.1.1-k8s1.11',
    'nfs_provisioner_version': 'v3.1.0-k8s1.11',
    'vsphere_csi_version': 'v1.0.3',
    'govc_version': 'v0.23.0',
    'rook_ceph_version': 'v1.3.6',
    'ceph_version': 'v14.2.9',
    'huawei_csi_driver_version': '2.2.9',
    'cinder_csi_version': 'v1.20.0',
    # rook csi
    'rook_csi_ceph_version': 'v2.1.2',
    'rook_csi_resizer_version': 'v0.4.0',
    'rook_csi_snapshotter_version': 'v1.2.2',
    'rook_csi_attacher_version': 'v2.1.0',
    'rook_csi_provisioner_version': 'v1.4.0',
    'rook_csi_node_driver_registrar_version': 'v1.2.0',
    # huawei csi
    'huawei_csi_attacher_version': 'v1.2.1',
    'huawei_csi_provisioner_version': 'v1.4.0',
    'huawei_csi_node_driver_registrar_version': 'v1.2.0',
    # vsphere csi
    'vsphere_csi_livenessprobe_version': 'v1.1.0',
    'vsphere_csi_attacher_version': 'v1.2.1',
    'vsphere_csi_provisioner_version': 'v1.4.0',
    'vsphere_csi_node_driver_registrar_version': 'v1.2.0',
    # cinder csi
    'cinder_csi_attacher_version': 'v3.1.0',
    'cinder_csi_provisioner_version': 'v2.1.1',
    'cinder_csi_snapshotter_version': 'v2.1.3',
    'cinder_csi_resizer_version': 'v1.1.0',
    'cinder_csi_livenessprobe_version': 'v2.1.0',
    'cinder_csi_node_driver_registrar_version': 'v1.3.0',
    # etcd版本
    'etcd_version':'v3.4.9',
    # docker版本
    'docker_version':'19.03.9',
    # containerd版本
    'containerd_version':'1.3.6',
    # flannel版本
    'flannel_version':'v0.12.0',
    # calico版本
    'calico_version':'v3.14.1',
    # coredns版本
    'coredns_version':'1.6.7',
    # helm v2 版本
    'helm_v2_version':'v2.16.9',
    # helm v3 版本
    'helm_v3_version':'v3.2.4',
    # nginx-ingress版本
    'nginx_ingress_version':'0.33.0',
    # traefik-ingress版本
    'traefik_ingress_version':'v2.2.1',
    # metrics-server版本
    'metrics_server_version':'v0.3.6',
    # istio版本
    'istio_version': '1.8.0'
}

v1_18_6 =  {
    'pause_version':  '3.2',
    'busybox_version': '1.28',
    'crictl_version': 'v1.18.0',
    'npd_version': 'v0.8.1',
    'kube_bench_version': 'v0.0.1',
    'runc_version': 'v1.0.0-rc91',
    'cni_version': 'v0.8.6',
    'cni_calico_version': 'v3.12.3',
    # 存储类镜像版本设置
    'rbd_provisioner_version': 'v2.1.1-k8s1.11',
    'nfs_provisioner_version': 'v3.1.0-k8s1.11',
    'vsphere_csi_version': 'v1.0.3',
    'govc_version': 'v0.23.0',
    'rook_ceph_version': 'v1.3.6',
    'ceph_version': 'v14.2.9',
    'huawei_csi_driver_version': '2.2.9',
    'cinder_csi_version': 'v1.20.0',
    # rook csi
    'rook_csi_ceph_version': 'v2.1.2',
    'rook_csi_resizer_version': 'v0.4.0',
    'rook_csi_snapshotter_version': 'v1.2.2',
    'rook_csi_attacher_version': 'v2.1.0',
    'rook_csi_provisioner_version': 'v1.4.0',
    'rook_csi_node_driver_registrar_version': 'v1.2.0',
    # huawei csi
    'huawei_csi_attacher_version': 'v1.2.1',
    'huawei_csi_provisioner_version': 'v1.4.0',
    'huawei_csi_node_driver_registrar_version': 'v1.2.0',
    # vsphere csi
    'vsphere_csi_livenessprobe_version': 'v1.1.0',
    'vsphere_csi_attacher_version': 'v1.2.1',
    'vsphere_csi_provisioner_version': 'v1.4.0',
    'vsphere_csi_node_driver_registrar_version': 'v1.2.0',
    # cinder csi
    'cinder_csi_attacher_version': 'v3.1.0',
    'cinder_csi_provisioner_version': 'v2.1.1',
    'cinder_csi_snapshotter_version': 'v2.1.3',
    'cinder_csi_resizer_version': 'v1.1.0',
    'cinder_csi_livenessprobe_version': 'v2.1.0',
    'cinder_csi_node_driver_registrar_version': 'v1.3.0',
    # etcd版本
    'etcd_version':'v3.4.9',
    # docker版本
    'docker_version':'19.03.9',
    # containerd版本
    'containerd_version':'1.3.6',
    # flannel版本
    'flannel_version':'v0.12.0',
    # calico版本
    'calico_version':'v3.14.1',
    # coredns版本
    'coredns_version':'1.6.7',
    # helm v2 版本
    'helm_v2_version':'v2.16.9',
    # helm v3 版本
    'helm_v3_version':'v3.2.4',
    # nginx-ingress版本
    'nginx_ingress_version':'0.33.0',
    # traefik-ingress版本
    'traefik_ingress_version':'v2.2.1',
    # metrics-server版本
    'metrics_server_version':'v0.3.6',
    # istio版本
    'istio_version': '1.8.0'
}

v1_18_8 =  {
    'pause_version':  '3.2',
    'busybox_version': '1.28',
    'crictl_version': 'v1.18.0',
    'npd_version': 'v0.8.1',
    'kube_bench_version': 'v0.0.1',
    'runc_version': 'v1.0.0-rc91',
    'cni_version': 'v0.8.6',
    'cni_calico_version': 'v3.12.3',
    # 存储类镜像版本设置
    'rbd_provisioner_version': 'v2.1.1-k8s1.11',
    'nfs_provisioner_version': 'v3.1.0-k8s1.11',
    'vsphere_csi_version': 'v1.0.3',
    'govc_version': 'v0.23.0',
    'rook_ceph_version': 'v1.3.6',
    'ceph_version': 'v14.2.9',
    'huawei_csi_driver_version': '2.2.9',
    'cinder_csi_version': 'v1.20.0',
    # rook csi
    'rook_csi_ceph_version': 'v2.1.2',
    'rook_csi_resizer_version': 'v0.4.0',
    'rook_csi_snapshotter_version': 'v1.2.2',
    'rook_csi_attacher_version': 'v2.1.0',
    'rook_csi_provisioner_version': 'v1.4.0',
    'rook_csi_node_driver_registrar_version': 'v1.2.0',
    # huawei csi
    'huawei_csi_attacher_version': 'v1.2.1',
    'huawei_csi_provisioner_version': 'v1.4.0',
    'huawei_csi_node_driver_registrar_version': 'v1.2.0',
    # vsphere csi
    'vsphere_csi_livenessprobe_version': 'v1.1.0',
    'vsphere_csi_attacher_version': 'v1.2.1',
    'vsphere_csi_provisioner_version': 'v1.4.0',
    'vsphere_csi_node_driver_registrar_version': 'v1.2.0',
    # cinder csi
    'cinder_csi_attacher_version': 'v3.1.0',
    'cinder_csi_provisioner_version': 'v2.1.1',
    'cinder_csi_snapshotter_version': 'v2.1.3',
    'cinder_csi_resizer_version': 'v1.1.0',
    'cinder_csi_livenessprobe_version': 'v2.1.0',
    'cinder_csi_node_driver_registrar_version': 'v1.3.0',
    # etcd版本
    'etcd_version':'v3.4.9',
    # docker版本
    'docker_version':'19.03.9',
    # containerd版本
    'containerd_version':'1.3.6',
    # flannel版本
    'flannel_version':'v0.12.0',
    # calico版本
    'calico_version':'v3.14.1',
    # coredns版本
    'coredns_version':'1.6.7',
    # helm v2 版本
    'helm_v2_version':'v2.16.9',
    # helm v3 版本
    'helm_v3_version':'v3.2.4',
    # nginx-ingress版本
    'nginx_ingress_version':'0.33.0',
    # traefik-ingress版本
    'traefik_ingress_version':'v2.2.1',
    # metrics-server版本
    'metrics_server_version':'v0.3.6',
    # istio版本
    'istio_version': '1.8.0'
}

v1_18_10 =  {
    'pause_version':  '3.2',
    'busybox_version': '1.28',
    'crictl_version': 'v1.18.0',
    'npd_version': 'v0.8.1',
    'kube_bench_version': 'v0.0.1',
    'runc_version': 'v1.0.0-rc91',
    'cni_version': 'v0.8.6',
    'cni_calico_version': 'v3.12.3',
    # 存储类镜像版本设置
    'rbd_provisioner_version': 'v2.1.1-k8s1.11',
    'nfs_provisioner_version': 'v3.1.0-k8s1.11',
    'vsphere_csi_version': 'v1.0.3',
    'govc_version': 'v0.23.0',
    'rook_ceph_version': 'v1.3.6',
    'ceph_version': 'v14.2.9',
    'huawei_csi_driver_version': '2.2.9',
    'cinder_csi_version': 'v1.20.0',
    # rook csi
    'rook_csi_ceph_version': 'v2.1.2',
    'rook_csi_resizer_version': 'v0.4.0',
    'rook_csi_snapshotter_version': 'v1.2.2',
    'rook_csi_attacher_version': 'v2.1.0',
    'rook_csi_provisioner_version': 'v1.4.0',
    'rook_csi_node_driver_registrar_version': 'v1.2.0',
    # huawei csi
    'huawei_csi_attacher_version': 'v1.2.1',
    'huawei_csi_provisioner_version': 'v1.4.0',
    'huawei_csi_node_driver_registrar_version': 'v1.2.0',
    # vsphere csi
    'vsphere_csi_livenessprobe_version': 'v1.1.0',
    'vsphere_csi_attacher_version': 'v1.2.1',
    'vsphere_csi_provisioner_version': 'v1.4.0',
    'vsphere_csi_node_driver_registrar_version': 'v1.2.0',
    # cinder csi
    'cinder_csi_attacher_version': 'v3.1.0',
    'cinder_csi_provisioner_version': 'v2.1.1',
    'cinder_csi_snapshotter_version': 'v2.1.3',
    'cinder_csi_resizer_version': 'v1.1.0',
    'cinder_csi_livenessprobe_version': 'v2.1.0',
    'cinder_csi_node_driver_registrar_version': 'v1.3.0',
    # etcd版本
    'etcd_version':'v3.4.9',
    # docker版本
    'docker_version':'19.03.9',
    # containerd版本
    'containerd_version':'1.3.6',
    # flannel版本
    'flannel_version':'v0.12.0',
    # calico版本
    'calico_version':'v3.14.1',
    # coredns版本
    'coredns_version':'1.6.7',
    # helm v2 版本
    'helm_v2_version':'v2.16.9',
    # helm v3 版本
    'helm_v3_version':'v3.2.4',
    # nginx-ingress版本
    'nginx_ingress_version':'0.33.0',
    # traefik-ingress版本
    'traefik_ingress_version':'v2.2.1',
    # metrics-server版本
    'metrics_server_version':'v0.3.6',
    # istio版本
    'istio_version': '1.8.0'
}

v1_18_12 =  {
    'pause_version':  '3.2',
    'busybox_version': '1.28',
    'crictl_version': 'v1.18.0',
    'npd_version': 'v0.8.1',
    'kube_bench_version': 'v0.0.1',
    'runc_version': 'v1.0.0-rc91',
    'cni_version': 'v0.8.6',
    'cni_calico_version': 'v3.12.3',
    # 存储类镜像版本设置
    'rbd_provisioner_version': 'v2.1.1-k8s1.11',
    'nfs_provisioner_version': 'v3.1.0-k8s1.11',
    'vsphere_csi_version': 'v1.0.3',
    'govc_version': 'v0.23.0',
    'rook_ceph_version': 'v1.3.6',
    'ceph_version': 'v14.2.9',
    'huawei_csi_driver_version': '2.2.9',
    'cinder_csi_version': 'v1.20.0',
    # rook csi
    'rook_csi_ceph_version': 'v2.1.2',
    'rook_csi_resizer_version': 'v0.4.0',
    'rook_csi_snapshotter_version': 'v1.2.2',
    'rook_csi_attacher_version': 'v2.1.0',
    'rook_csi_provisioner_version': 'v1.4.0',
    'rook_csi_node_driver_registrar_version': 'v1.2.0',
    # huawei csi
    'huawei_csi_attacher_version': 'v1.2.1',
    'huawei_csi_provisioner_version': 'v1.4.0',
    'huawei_csi_node_driver_registrar_version': 'v1.2.0',
    # vsphere csi
    'vsphere_csi_livenessprobe_version': 'v1.1.0',
    'vsphere_csi_attacher_version': 'v1.2.1',
    'vsphere_csi_provisioner_version': 'v1.4.0',
    'vsphere_csi_node_driver_registrar_version': 'v1.2.0',
    # cinder csi
    'cinder_csi_attacher_version': 'v3.1.0',
    'cinder_csi_provisioner_version': 'v2.1.1',
    'cinder_csi_snapshotter_version': 'v2.1.3',
    'cinder_csi_resizer_version': 'v1.1.0',
    'cinder_csi_livenessprobe_version': 'v2.1.0',
    'cinder_csi_node_driver_registrar_version': 'v1.3.0',
    # etcd版本
    'etcd_version':'v3.4.9',
    # docker版本
    'docker_version':'19.03.9',
    # containerd版本
    'containerd_version':'1.4.1',
    # flannel版本
    'flannel_version':'v0.13.0',
    # calico版本
    'calico_version':'v3.16.5',
    # coredns版本
    'coredns_version':'1.8.0',
    # helm v2 版本
    'helm_v2_version':'v2.17.0',
    # helm v3 版本
    'helm_v3_version':'v3.4.1',
    # nginx-ingress版本
    'nginx_ingress_version':'0.33.0',
    # traefik-ingress版本
    'traefik_ingress_version':'v2.2.1',
    # metrics-server版本
    'metrics_server_version':'v0.3.6',
    # istio版本
    'istio_version': '1.8.0'
}

v1_18_14 =  {
    'pause_version':  '3.2',
    'busybox_version': '1.28',
    'crictl_version': 'v1.18.0',
    'npd_version': 'v0.8.1',
    'kube_bench_version': 'v0.0.1',
    'runc_version': 'v1.0.0-rc91',
    'cni_version': 'v0.8.6',
    'cni_calico_version': 'v3.12.3',
    # 存储类镜像版本设置
    'rbd_provisioner_version': 'v2.1.1-k8s1.11',
    'nfs_provisioner_version': 'v3.1.0-k8s1.11',
    'vsphere_csi_version': 'v1.0.3',
    'govc_version': 'v0.23.0',
    'rook_ceph_version': 'v1.3.6',
    'ceph_version': 'v14.2.9',
    'huawei_csi_driver_version': '2.2.9',
    'cinder_csi_version': 'v1.20.0',
    # rook csi
    'rook_csi_ceph_version': 'v2.1.2',
    'rook_csi_resizer_version': 'v0.4.0',
    'rook_csi_snapshotter_version': 'v1.2.2',
    'rook_csi_attacher_version': 'v2.1.0',
    'rook_csi_provisioner_version': 'v1.4.0',
    'rook_csi_node_driver_registrar_version': 'v1.2.0',
    # huawei csi
    'huawei_csi_attacher_version': 'v1.2.1',
    'huawei_csi_provisioner_version': 'v1.4.0',
    'huawei_csi_node_driver_registrar_version': 'v1.2.0',
    # vsphere csi
    'vsphere_csi_livenessprobe_version': 'v1.1.0',
    'vsphere_csi_attacher_version': 'v1.2.1',
    'vsphere_csi_provisioner_version': 'v1.4.0',
    'vsphere_csi_node_driver_registrar_version': 'v1.2.0',
    # cinder csi
    'cinder_csi_attacher_version': 'v3.1.0',
    'cinder_csi_provisioner_version': 'v2.1.1',
    'cinder_csi_snapshotter_version': 'v2.1.3',
    'cinder_csi_resizer_version': 'v1.1.0',
    'cinder_csi_livenessprobe_version': 'v2.1.0',
    'cinder_csi_node_driver_registrar_version': 'v1.3.0',
    # etcd版本
    'etcd_version':'v3.4.14',
    # docker版本
    'docker_version':'19.03.9',
    # containerd版本
    'containerd_version':'1.4.3',
    # flannel版本
    'flannel_version':'v0.13.0',
    # calico版本
    'calico_version':'v3.16.5',
    # coredns版本
    'coredns_version':'1.8.0',
    # helm v2 版本
    'helm_v2_version':'v2.17.0',
    # helm v3 版本
    'helm_v3_version':'v3.4.1',
    # nginx-ingress版本
    'nginx_ingress_version':'0.33.0',
    # traefik-ingress版本
    'traefik_ingress_version':'v2.2.1',
    # metrics-server版本
    'metrics_server_version':'v0.3.6',
    # istio版本
    'istio_version': '1.8.0'
}

v1_18_15 =  {
    'pause_version':  '3.2',
    'busybox_version': '1.28',
    'crictl_version': 'v1.18.0',
    'npd_version': 'v0.8.1',
    'kube_bench_version': 'v0.0.1',
    'runc_version': 'v1.0.0-rc91',
    'cni_version': 'v0.8.6',
    'cni_calico_version': 'v3.12.3',
    # 存储类镜像版本设置
    'rbd_provisioner_version': 'v2.1.1-k8s1.11',
    'nfs_provisioner_version': 'v3.1.0-k8s1.11',
    'vsphere_csi_version': 'v1.0.3',
    'govc_version': 'v0.23.0',
    'rook_ceph_version': 'v1.3.6',
    'ceph_version': 'v14.2.9',
    'huawei_csi_driver_version': '2.2.9',
    'cinder_csi_version': 'v1.20.0',
    # rook csi
    'rook_csi_ceph_version': 'v2.1.2',
    'rook_csi_resizer_version': 'v0.4.0',
    'rook_csi_snapshotter_version': 'v1.2.2',
    'rook_csi_attacher_version': 'v2.1.0',
    'rook_csi_provisioner_version': 'v1.4.0',
    'rook_csi_node_driver_registrar_version': 'v1.2.0',
    # huawei csi
    'huawei_csi_attacher_version': 'v1.2.1',
    'huawei_csi_provisioner_version': 'v1.4.0',
    'huawei_csi_node_driver_registrar_version': 'v1.2.0',
    # vsphere csi
    'vsphere_csi_livenessprobe_version': 'v1.1.0',
    'vsphere_csi_attacher_version': 'v1.2.1',
    'vsphere_csi_provisioner_version': 'v1.4.0',
    'vsphere_csi_node_driver_registrar_version': 'v1.2.0',
    # cinder csi
    'cinder_csi_attacher_version': 'v3.1.0',
    'cinder_csi_provisioner_version': 'v2.1.1',
    'cinder_csi_snapshotter_version': 'v2.1.3',
    'cinder_csi_resizer_version': 'v1.1.0',
    'cinder_csi_livenessprobe_version': 'v2.1.0',
    'cinder_csi_node_driver_registrar_version': 'v1.3.0',
    # etcd版本
    'etcd_version':'v3.4.14',
    # docker版本
    'docker_version':'19.03.9',
    # containerd版本
    'containerd_version':'1.4.3',
    # flannel版本
    'flannel_version':'v0.13.0',
    # calico版本
    'calico_version':'v3.16.5',
    # coredns版本
    'coredns_version':'1.8.0',
    # helm v2 版本
    'helm_v2_version':'v2.17.0',
    # helm v3 版本
    'helm_v3_version':'v3.4.1',
    # nginx-ingress版本
    'nginx_ingress_version':'0.33.0',
    # traefik-ingress版本
    'traefik_ingress_version':'v2.2.1',
    # metrics-server版本
    'metrics_server_version':'v0.3.6',
    # istio版本
    'istio_version': '1.8.0'
}

v1_20_4 =  {
    'pause_version':  '3.2',
    'busybox_version': '1.28',
    'crictl_version': 'v1.18.0',
    'npd_version': 'v0.8.1',
    'kube_bench_version': 'v0.0.1',
    'runc_version': 'v1.0.0-rc91',
    'cni_version': 'v0.8.6',
    'cni_calico_version': 'v3.12.3',
    # 存储类镜像版本设置
    'rbd_provisioner_version': 'v2.1.1-k8s1.11',
    'nfs_provisioner_version': 'v3.1.0-k8s1.11',
    'vsphere_csi_version': 'v1.0.3',
    'govc_version': 'v0.23.0',
    'rook_ceph_version': 'v1.3.6',
    'ceph_version': 'v14.2.9',
    'huawei_csi_driver_version': '2.2.9',
    'cinder_csi_version': 'v1.20.0',
    # rook csi
    'rook_csi_ceph_version': 'v2.1.2',
    'rook_csi_resizer_version': 'v0.4.0',
    'rook_csi_snapshotter_version': 'v1.2.2',
    'rook_csi_attacher_version': 'v2.1.0',
    'rook_csi_provisioner_version': 'v1.4.0',
    'rook_csi_node_driver_registrar_version': 'v1.2.0',
    # huawei csi
    'huawei_csi_attacher_version': 'v1.2.1',
    'huawei_csi_provisioner_version': 'v1.4.0',
    'huawei_csi_node_driver_registrar_version': 'v1.2.0',
    # vsphere csi
    'vsphere_csi_livenessprobe_version': 'v1.1.0',
    'vsphere_csi_attacher_version': 'v1.2.1',
    'vsphere_csi_provisioner_version': 'v1.4.0',
    'vsphere_csi_node_driver_registrar_version': 'v1.2.0',
    # cinder csi
    'cinder_csi_attacher_version': 'v3.1.0',
    'cinder_csi_provisioner_version': 'v2.1.1',
    'cinder_csi_snapshotter_version': 'v2.1.3',
    'cinder_csi_resizer_version': 'v1.1.0',
    'cinder_csi_livenessprobe_version': 'v2.1.0',
    'cinder_csi_node_driver_registrar_version': 'v1.3.0',
    # etcd版本
    'etcd_version':'v3.4.14',
    # docker版本
    'docker_version':'19.03.9',
    # containerd版本
    'containerd_version':'1.4.3',
    # flannel版本
    'flannel_version':'v0.13.0',
    # calico版本
    'calico_version':'v3.16.5',
    # coredns版本
    'coredns_version':'1.8.0',
    # helm v2 版本
    'helm_v2_version':'v2.17.0',
    # helm v3 版本
    'helm_v3_version':'v3.4.1',
    # nginx-ingress版本
    'nginx_ingress_version':'0.33.0',
    # traefik-ingress版本
    'traefik_ingress_version':'v2.2.1',
    # metrics-server版本
    'metrics_server_version':'v0.3.6',
    # istio版本
    'istio_version': '1.8.0'
}