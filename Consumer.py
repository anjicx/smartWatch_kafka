from confluent_kafka import Consumer, KafkaError
import json
from Connection import create_connection, insert_heart_data, insert_blood_pressure_data, insert_oxygen_data, insert_activity_data, insert_sleep_data

kafka_bootstrap_servers = "localhost:9092"
consumer_group = "health_data_group"
topics = ["heart_data", "blood_pressure_data", "oxygen_data", "activity_data", "sleep_data"]

def create_consumer(group_id):
    return Consumer({
        'bootstrap.servers': kafka_bootstrap_servers,  
        'group.id': group_id,  
        'auto.offset.reset': 'earliest'  
    })

def handle_kafka_message(topic, message, cursor):
    data = json.loads(message.value().decode('utf-8'))

    if topic == "heart_data":
        insert_heart_data(cursor, (data["Timestamp"], data["Heart Rate (BPM)"], data["Stress Level (0-100)"]))
    elif topic == "blood_pressure_data":
        insert_blood_pressure_data(cursor, (data["Timestamp"], data["Systolic BP"], data["Diastolic BP"]))
    elif topic == "oxygen_data":
        insert_oxygen_data(cursor, (data["Timestamp"], data["SpO2 (%)"]))
    elif topic == "activity_data":
        insert_activity_data(cursor, (data["Timestamp"], data["Steps"], data["Calories Burned"]))
    elif topic == "sleep_data":
        insert_sleep_data(cursor, (data["Timestamp"], data["Sleep Quality (0-100)"]))

def consume_messages():
    consumer = create_consumer(consumer_group)
    consumer.subscribe(topics)
    print(f"Subscribed to topics: {topics}")

    conn = create_connection()
    if conn is None:
        print("Failed to connect to database.")
        return

    cursor = conn.cursor()  

    try:
        while True:  
            msg = consumer.poll(1.0)  
            if msg is None:
                continue  
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print("End of partition reached.")
                else:
                    print(f"Error: {msg.error()}")
            else:
                print(f"Consumed message from {msg.topic()}: {msg.value()}")
                try:
                   
                    handle_kafka_message(msg.topic(), msg, cursor)
                    conn.commit()  
                except Exception as e:
                    print(f"Error processing message: {e}")
                    conn.rollback()  
    except KeyboardInterrupt:
        print("Consumer stopped.")
    finally:
        cursor.close()
        conn.close()
        consumer.close()
        print("Connection to database and Kafka closed.")

consume_messages()
