images = {
    'coredns_image': '{local_hostname}:{registry_port}/coredns/coredns:{coredns_version}',
    'sandbox_image': '{local_hostname}:{registry_port}/kubeoperator/pause:{pause_version}-{architectures}',
    'busybox_image': '{local_hostname}:{registry_port}/kubeoperator/busybox:{busybox_version}-{architectures}'
}