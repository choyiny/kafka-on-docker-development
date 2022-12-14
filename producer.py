from datetime import datetime
from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers=['localhost:9093'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

if __name__ == "__main__":
    future = producer.send('posts', {
        "author": "choyiny",
        "content": "Hello World!",
        # interestingly, clickhouse does not support isoformat() with milliseconds
        "created_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    })
    future.get(timeout=1)
