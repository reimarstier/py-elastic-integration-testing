# Kafka Docker Images
https://hub.docker.com/r/confluentinc/cp-kafka
https://rmoff.net/2018/08/02/kafka-listeners-explained/
https://docs.confluent.io/current/installation/docker/image-reference.html#image-reference

# Kafka useful commands
kafka-console-producer --broker-list kafka:9092 --topic test
kafka-topics --zookeeper zookeeper --list
kafka-console-consumer --bootstrap-server kafka:9092 --topic test --from-beginning
