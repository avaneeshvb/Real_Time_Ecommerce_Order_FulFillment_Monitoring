from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers="redpanda:9092",
    value_serializer=lambda v: json.dumps(v).encode()
)


def publish(event):
    producer.send("ecommerce_events", event)
    producer.flush()