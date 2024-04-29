import paho.mqtt.client as mqtt
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
# MQTT client configuration
mqtt_host = 'localhost'
mqtt_port = 1883
mqtt_topic = 'sensors.temperature'  # This should match the RabbitMQ routing key

try:
    # Create the MQTT client
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

    # Connect to the MQTT broker (RabbitMQ with MQTT plugin)
    client.connect(mqtt_host, mqtt_port, 60)

    # Publish a message to RabbitMQ via MQTT
    test_message = '{"sensor_id": "1212","temperature": 22.5,"timestamp": "2024-04-29T10:30:00"}'
    client.publish(mqtt_topic, test_message)

    logging.info("Published to RabbitMQ via MQTT")
    # Disconnect the client
    client.disconnect()
    
except Exception as e:
    logging.info(e)