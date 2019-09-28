from kafka import KafkaConsumer, KafkaProducer, KafkaClient


producer = KafkaProducer(bootstrap_servers='localhost:9092')

for i in range(100):
    input_string = input('>>')
    future = producer.send('test', input_string.encode())
    r = future.get(timeout=60)
    print(r)
