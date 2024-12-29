from confluent_kafka import Producer
import pandas as pd
import json
import time

csv_file = "C:\python\simulated_health_data_minute.csv"  
data = pd.read_csv(csv_file)

topics = {
    "heart_data": ["Timestamp", "Heart Rate (BPM)", "Stress Level (0-100)"],
    "blood_pressure_data": ["Timestamp", "Systolic BP", "Diastolic BP"],
    "oxygen_data": ["Timestamp", "SpO2 (%)"],
    "activity_data": ["Timestamp", "Steps", "Calories Burned"],
    "sleep_data": ["Timestamp", "Sleep Quality (0-100)"]
}

kafka_bootstrap_servers = "localhost:9092" 
def create_producer():
    return Producer({'bootstrap.servers': kafka_bootstrap_servers})

def send_message_to_kafka(producer, topic, message):
    producer.produce(topic, value=json.dumps(message))
    print(f"Sent to {topic}: {message}")

def produce_messages(producer, data, topics):
    for index, row in data.iterrows():  
       
        for topic, columns in topics.items():  
            message = row[columns].to_dict()
            send_message_to_kafka(producer, topic, message)
        producer.flush()  
        time.sleep(0.1)  

producer = create_producer()
produce_messages(producer, data, topics)
