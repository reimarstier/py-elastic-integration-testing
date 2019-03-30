# Kafka Docker Images
https://hub.docker.com/r/confluentinc/cp-kafka

# Kafka useful commands
kafka-console-producer --broker-list kafka:9092 --topic test
kafka-topics --zookeeper zookeeper --list
kafka-console-consumer --bootstrap-server kafka:9092 --topic test --from-beginning
