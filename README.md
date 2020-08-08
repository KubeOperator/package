# KubeOperator 3.0 离线安装包工程

KubeOperator 3.0 支持在线和离线环境下部署 K8s 集群。KubeOperator 内置 Nexus 服务，用来提供部署和管理 K8s 所需要的介质，包括：

- 镜像
- rpm
- 二进制文件

## 在线模式

该模式下，KubeOperator 内置 Nexus 服务讲在线方式同步并下载所需的文件。

## 离线模式

本工程将构建离线环境的部署包，并导入到 KubeOperator 内置 Nexus 服务。
