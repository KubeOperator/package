#!/usr/bin/env python3
# coding: utf-8

# kubernetes 版本管理
def version_mg(vs):
    v = {
        'v1.18.15': v1_18_15,
    }
    return v.get(vs,'none version')

v1_18_15 =  {
    # pod 基础镜像版本
    'pause_version':  '3.2',
    # cni 版本
    'cni_version': 'v0.8.6',
    # etcd 版本
    'etcd_version':'v3.4.14',
    # docker版本
    'docker_version':'19.03.9',
    # calico版本
    'calico_version':'v3.16.5',
    # coredns版本
    'coredns_version':'1.8.0',
    # helm v3 版本
    'helm_v3_version':'v3.4.1',
    # nginx-ingress版本
    'nginx_ingress_version':'0.33.0',
    # metrics-server版本
    'metrics_server_version':'v0.3.6'
}