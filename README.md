#  Real-Time Health Data Processing System

# Overview

This project simulates a real-time health data processing system using Python and Apache Kafka. It models how wearable device data (such as heart rate, blood pressure, oxygen saturation, activity, and sleep quality) can be collected, distributed, processed, and stored in a relational database.

# SYSTEM ARCHITECTURE

The system consists of three main components:
1. Data Generation - Simulated health data is read from a CSV file and sent to Kafka.
2. Data Distribution via Apache Kafka - Data is streamed to five Kafka topics, each corresponding to a specific type of health metric.
3. Data Storage in MySQL Database - A Kafka consumer retrieves the data, processes it, and stores it efficiently.

# KEY FEATURES:

~ Simulated health data generation using a CSV file.

~ Kafka-based data streaming, with separate topics for different data types.

~ Real-time data processing, ensuring efficient message handling and storage.

~ MySQL database integration, optimized for structured health data storage.


# TECHNOLOGIES USED:

~Python (data generation, Kafka producer & consumer)

~Apache Kafka (message broker for distributed data processing)

~MySQL (relational database for structured storage)

~Confluent Kafka Python library (Kafka integration)

~Pandas (data manipulation and analysis).



# PREREQUISITES:

~Apache Kafka installed and running

~Python 3.x installed

~MySQL Server running on port 3307


# POTENTIAL USE CASES:

~Real-time health monitoring systems - Continuously track vital signs and detect anomalies using real-time Kafka streams.

~IoT-based patient tracking - Integrate with wearable devices to monitor patient activity, heart rate, and other key health metrics.

~Data-driven medical insights - Process large volumes of patient data to identify trends and support clinical decision-making.

~Remote healthcare solutions - Enable telemedicine platforms by providing real-time health data for remote patient care.
