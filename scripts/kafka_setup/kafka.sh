# from https://knowledge.udacity.com/questions/685481
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm template kafka bitnami/kafka \
     --set volumePermissions.enabled=true \
     --set zookeeper.volumePermissions.enabled=true \
     > deployment/kafka.yaml