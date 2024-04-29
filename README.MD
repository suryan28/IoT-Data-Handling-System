# Processing MQTT Messages via RabbitMQ

## Introduction

This Python script is designed to process incoming MQTT messages via RabbitMQ and save them to a MongoDB database.

## Technologies Used
- Python
- MQTT
- RabbitMQ
- MongoDB


## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/suryan28/IoT-Data-Handling-System.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd IoT-Data-Handling-System
   ```
3. **Create virtual environment:**
   ```bash
   virtualenv -p python3.8 env_name
   ```
4. **Activate virtual environment:**
   ```bash
   source env_name/bin/activate
   ```
5. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
6. **Run 'main.py' to activate rabbitmq channel:**
   ```bash
   python main.py 
   ```
7. **Open a new terminal and execute the 'mqtt_msg_publish.py' script:**
   ```bash
   python mqtt_msg_publish.py
   ```


