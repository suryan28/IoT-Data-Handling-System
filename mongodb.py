from pymongo import MongoClient
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# MongoDB configuration
mongodb_host = 'localhost'
mongodb_port = 27017
mongodb_database = 'iot_data_db'
mongodb_collection = 'sensor_data'
mongo_client = MongoClient(mongodb_host, mongodb_port)
db = mongo_client[mongodb_database]
collection = db[mongodb_collection]

def save_to_mongodb(data):
    try:
        result = collection.insert_one(data)
        logging.info(f"Inserted ID: {result.inserted_id}")
        return True
    except Exception as e:
        logging.info(f"Error inserting into MongoDB: {e}")
        return False


# mosquitto_pub -h 'localhost' -p '1883' -t "sensors/temperature" -m '{"location": "room1", "temperature": 22.5}'