from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.serialization import SimpleStringSchema
from pyflink.datastream.connectors import FlinkKafkaConsumer
import json
from datetime import datetime, timedelta

env = StreamExecutionEnvironment.get_execution_environment()
env.set_parallelism(1)

consumer_props = {
    'bootstrap.servers': 'redpanda:9092',
    'group.id': 'sla-group'
}

consumer = FlinkKafkaConsumer(
    topics='ecommerce_events',
    deserialization_schema=SimpleStringSchema(),
    properties=consumer_props
)

stream = env.add_source(consumer)


# state (simplified for Zoomcamp clarity)
orders = {}
fulfillments = {}


def process(event_str):
    event = json.loads(event_str)

    if event["event_type"] == "order":
        orders[event["order_id"]] = event

    if event["event_type"] == "fulfillment":
        fulfillments[event["order_id"]] = event

    # SLA BREACH LOGIC
    now = datetime.utcnow()

    alerts = []

    for oid, order in orders.items():
        if oid not in fulfillments:
            order_time = datetime.fromisoformat(order["created_at"].replace("Z",""))
            if now - order_time > timedelta(hours=6):
                alerts.append(f"SLA_BREACH:{oid}")

    for a in alerts:
        print(a)


stream.map(process)

env.execute("SLA Job")

