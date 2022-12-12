from flask import Flask, request
from kafka import KafkaProducer
from datetime import datetime
import json

app = Flask(__name__)
producer = KafkaProducer(
    bootstrap_servers=['localhost:9093'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# curl -X POST -H "Content-Type: application/json" -d '{"author": "choyiny", "content": "Kafka is cool!"}' http://localhost:5000/posts
@app.route('/posts', methods=['POST'])
def create_post():
    post = request.get_json()  # {'author': 'choyiny', 'content': 'Kafka is cool!'}
    post['created_at'] = datetime.now().isoformat()
    producer.send('posts', post)
    return 'ok'
