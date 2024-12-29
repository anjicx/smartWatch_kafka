from confluent_kafka import Producer
import pandas as pd
import json
import time

# Čitanje CSV fajla
csv_file = "C:\python\simulated_health_data_minute.csv"  # Putanja do CSV fajla (koristi 'r' za raw string)
data = pd.read_csv(csv_file)#podaci iz fajla učitani u DataFrame

# Teme za različite grupe podataka
#U rečniku je ključ naziv teme, a vrednost je lista stringova koji su nazivi kolona
topics = {
    "heart_data": ["Timestamp", "Heart Rate (BPM)", "Stress Level (0-100)"],
    "blood_pressure_data": ["Timestamp", "Systolic BP", "Diastolic BP"],
    "oxygen_data": ["Timestamp", "SpO2 (%)"],
    "activity_data": ["Timestamp", "Steps", "Calories Burned"],
    "sleep_data": ["Timestamp", "Sleep Quality (0-100)"]
}

kafka_bootstrap_servers = "localhost:9092"  # Adresa Kafka servera
#kreiranje objekta klase Producer
def create_producer():
    return Producer({'bootstrap.servers': kafka_bootstrap_servers})

#funkcija za slanje podataka u kreiranu temu
def send_message_to_kafka(producer, topic, message):
    producer.produce(topic, value=json.dumps(message))
    #funkcija produce kafkine bibliot confluent_kafka koja salje poruku JSON string verzije u topic
    print(f"Sent to {topic}: {message}")

def produce_messages(producer, data, topics):
    # Prolazimo kroz sve redove data koristeći funkciju iterrows.
    # iterrows() vraća tuple u kojem je prvi element index (broj reda), a drugi element row 
    for index, row in data.iterrows():  
       
        for topic, columns in topics.items():  
            #topic su ključevi rečnika topics, a columns je vrednost u recniku(lista kolona svakog topika)
            # Koristimo 'row[columns]' da izvučemo podatke iz 'row' koji su vezani za kolone konkretne teme
            # Ovako dobijeni pandas Series objekat pretvaramo u pravi Python rečnik sa to_dict() funkcijom
            message = row[columns].to_dict()
            # Pozivamo funkciju za slanje poruke Kafka serveru. 
            # 'producer' je Kafka producer objekat koji šalje poruke u Kafka teme.
            send_message_to_kafka(producer, topic, message)  
        # Pozivom producer.flush() osiguravamo da su sve poruke zaista poslate na Kafka server.
        # 'flush()' će sačekati da se sve poruke završe pre nego što nastavi dalje.
        producer.flush()  
        # Simulacija kašnjenja između slanja poruka.
        time.sleep(0.1)  

#pozivi funkcija
producer = create_producer()#producer iz kafka biblioteke
#data pomoću pandas pročitani csv fajl 
produce_messages(producer, data, topics)
