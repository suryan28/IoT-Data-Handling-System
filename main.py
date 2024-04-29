import pika
import mongodb, data_transform
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
# RabbitMQ configuration
rabbitmq_host = 'localhost'
rabbitmq_queue = 'my_mqtt_queue'

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
channel = connection.channel()

# Declare the queue before consuming
queue_name = 'my_mqtt_queue'
channel.queue_declare(queue=queue_name, durable=True)

# Callback function for processing messages
def callback(ch, method, properties, body):
    """Callback function for processing messages."""
    try:
        data = {
            'routing_key': method.routing_key,
            'message_body': body,
            'properties': {
                'content_type': properties.content_type,
                'delivery_mode': properties.delivery_mode
            }
        }
        # Calling 'process_message' function to get clean data.
        clean_data = data_transform.process_message(data["message_body"])
        if clean_data:
            # Calling 'save_to_mongodb' function for inserting data into mongo db.
            status = mongodb.save_to_mongodb(clean_data)
            if status:
                logging.info(f"Stored in MongoDB: {data}")
            else:
                logging.info("Facing issue while inserting data in MongoDB.")
    except Exception as e:
        logging.info(e)

# Start consuming messages
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
logging.info("Waiting for messages...")

channel.queue_bind(exchange='amq.topic', queue=queue_name, routing_key='sensors.temperature')

channel.start_consuming()
