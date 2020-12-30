# KubeOpererator 3.0 离线部署包

KubeOperator 3.0 支持在完全离线环境下部署 K8s 集群。KubeOperator 内置 Nexus 服务，用来提供部署和管理 K8s 所需要的介质，包括：

- Docker 镜像
- Rpm 包
- 二进制文件等

本工程将构建离线环境下所需的介质，并导入到 KubeOperator 内置 Nexus 制品库。

使用: `# python3 build.py kube_version kube_upgrade_version`

例:   `# python3 build.py v1.18.6 v1.18.10 `