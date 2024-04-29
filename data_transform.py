import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def process_message(message):
    try:
        # Convert message payload to JSON
        json_data = json.loads(message)
        # Validate or transform data here
        # logging.info("Validated message:", json_data)
        return json_data
    except json.JSONDecodeError:
        logging.info("Error decoding JSON")
        return None
    except Exception as e:
        logging.info(f"Error processing message: {e}")
        return None
