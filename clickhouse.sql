CREATE TABLE default.message_queue
(
  created_at DateTime,
  content String
)
  ENGINE = Kafka(
    'kafka:9092',
    'posts',
    'clickhouse',
    'JSONEachRow'
  ) settings kafka_thread_per_consumer = 0, kafka_num_consumers = 1;

CREATE TABLE default.messages
(
  created_at DateTime,
  content String
)
  ENGINE = MergeTree
  ORDER BY created_at;

CREATE MATERIALIZED VIEW default.messages_mv
  TO default.messages
  AS SELECT * FROM default.message_queue;