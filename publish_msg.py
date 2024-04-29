import pika
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
# RabbitMQ configuration
rabbitmq_host = 'localhost'
rabbitmq_queue = 'my_mqtt_queue'
routing_key = 'sensors.temperature'

# Connect to RabbitMQ
try:
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
    channel = connection.channel()
    # Declare the queue to ensure it exists
    channel.queue_declare(queue=rabbitmq_queue, durable=True)
    # Create a test message to publish
    test_message = '{"sensor_id": "123","temperature": 22.5,"timestamp": "2024-04-29T10:30:00"}'
    # Publish the test message to the queue
    channel.basic_publish(
        exchange='amq.topic',
        routing_key=routing_key,
        body=test_message,
        properties=pika.BasicProperties(
            content_type='application/json',
            delivery_mode=2  
        )
    )
    logging.info("Test message published to RabbitMQ")
    # Close the connection
    connection.close()

except Exception as e:
    logging.info(e)