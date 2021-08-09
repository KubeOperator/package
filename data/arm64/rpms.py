#!/usr/bin/env python3
# coding: utf-8

deb_base={
    'ceph-common',
    'nfs-common',
    'jq',
    'conntrack',
    'bash-completion',
    'libseccomp2',
    'psmisc',
    'rsync',
    'socat',
    'ipset',
    'ipvsadm',
    'haproxy',
    'chrony',
    'lvm2',
    'open-iscsi',
    'kpartx',
    'sshpass',
    'python-apt',
    'keepalived',
}

centos_rpms_base={
    'bash-completion',
    'chrony',
    'conntrack-tools',
    'dnsmasq',
    'ipset',
    'ipset-libs',
    'ipvsadm',
    'nfs-utils',
    'ntpdate',
    'psmisc',
    'rpcbind',
    'rsync',
    'socat',
    'keyutils',
    'libbasicobjects',
    'gssproxy',
    'libevent',
    'libcollection',
    'libpath_utils',
    'libini_config',
    'libtirpc',
    'libnfsidmap',
    'libref_array',
    'quota',
    'libverto-libevent',
    'quota-nls',
    'tcp_wrappers',
    'libseccomp',
    'libnetfilter_cttimeout',
    'libnetfilter_cthelper',
    'libnetfilter_queue',
    'jq',
    'oniguruma',
    'haproxy',
    'ceph-common',
    'at',
    'avahi-libs',
    'bc',
    'boost-iostreams',
    'boost-program-options',
    'boost-random',
    'boost-regex',
    'boost-system',
    'boost-thread',
    'cryptsetup',
    'cups-client',
    'cups-libs',
    'ed',
    'gdisk',
    'hdparm',
    'json-c',
    'libicu',
    'librados2',
    'librbd1',
    'm4',
    'mailx',
    'patch',
    'psmisc',
    'python-backports',
    'python-backports-ssl_match_hostname',
    'python-chardet',
    'python-ipaddress',
    'python-rados',
    'python-rbd',
    'python-requests',
    'python-six',
    'python-urllib3',
    'redhat-lsb-core',
    'redhat-lsb-submod-security',
    'spax',
    'time',
    'cryptsetup-libs',
    'iscsi-initiator-utils',
    'iscsi-initiator-utils-iscsiuio',
    'device-mapper',
    'device-mapper-event',
    'device-mapper-multipath',
    'lvm2',
    'kpartx',
    'sshpass',
    'attr',
    'glusterfs',
    'glusterfs-libs',
    'glusterfs-fuse',
    'glusterfs-client-xlators',
    'keepalived',
    'lm_sensors-libs',
    'net-snmp-agent-libs',
    'net-snmp-libs',
}