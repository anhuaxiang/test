from kafka import KafkaConsumer, KafkaProducer, KafkaClient, TopicPartition


# consumer = KafkaConsumer('test', bootstrap_servers='localhost:9092')
# for r in consumer:
#     print(r)


consumer = KafkaConsumer(bootstrap_servers='localhost:9092')
consumer.assign([TopicPartition('test', 0)])
consumer.seek(TopicPartition('test', 0), 0)
while True:
    msg = next(consumer)
    print(msg)

