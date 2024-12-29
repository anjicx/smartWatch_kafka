from confluent_kafka import Consumer, KafkaError
import json
from Connection import create_connection, insert_heart_data, insert_blood_pressure_data, insert_oxygen_data, insert_activity_data, insert_sleep_data

# 1. Konfiguracija Kafka servera i grupa potrošača
kafka_bootstrap_servers = "localhost:9092"
consumer_group = "health_data_group"
topics = ["heart_data", "blood_pressure_data", "oxygen_data", "activity_data", "sleep_data"]

# 2. Kreiranje Kafka consumera
def create_consumer(group_id):
    # Povezivanje sa Kafka serverom i definisanje parametara potrošača
    return Consumer({
        'bootstrap.servers': kafka_bootstrap_servers,  # Adresa Kafka servera
        'group.id': group_id,  # Grupa potrošača za deljenje rada
        'auto.offset.reset': 'earliest'  # Čitanje poruka od početka
    })

# 3. Funkcija za obradu poruka i unos u bazu
def handle_kafka_message(topic, message, cursor):
    # Konvertovanje poruke iz JSON formata
    data = json.loads(message.value().decode('utf-8'))

    # Obrada na osnovu teme (topic)
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

# 4. Funkcija za preuzimanje i obradu poruka
def consume_messages():
    # Kreiranje Kafka consumera i pretplata na teme
    consumer = create_consumer(consumer_group)
    consumer.subscribe(topics)
    print(f"Subscribed to topics: {topics}")

    # Konekcija sa bazom
    conn = create_connection()
    if conn is None:
        print("Failed to connect to database.")
        return

    cursor = conn.cursor()  # Kreiranje kursora za SQL komande

    try:
        while True:  # Neprekidna petlja za obradu poruka
            msg = consumer.poll(1.0)  # Čekanje poruke do 1 sekunde
            if msg is None:
                continue  # Nema novih poruka
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print("End of partition reached.")
                else:
                    print(f"Error: {msg.error()}")
            else:
                print(f"Consumed message from {msg.topic()}: {msg.value()}")
                try:
                    # Obrada poruke i unos u bazu
                    handle_kafka_message(msg.topic(), msg, cursor)
                    conn.commit()  # Sačuvaj promene u bazi
                except Exception as e:
                    print(f"Error processing message: {e}")
                    conn.rollback()  # Vraćanje unazad u slučaju greške
    except KeyboardInterrupt:
        # Prekid programa od strane korisnika (Ctrl+C)
        print("Consumer stopped.")
    finally:
        # Zatvaranje resursa
        cursor.close()
        conn.close()
        consumer.close()
        print("Connection to database and Kafka closed.")

# 5. Pokretanje programa
consume_messages()
