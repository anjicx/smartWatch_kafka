Real-Time Health Data Processing System

Overview

This project simulates a real-time health data processing system using Python and Apache Kafka. It models how wearable device data (such as heart rate, blood pressure, oxygen saturation, activity, and sleep quality) can be collected, distributed, processed, and stored in a relational database.

SYSTEM ARCHITECTURE

The system consists of three main components:
1. Data Generation
2. Data Distribution via Apache Kafka
3. Data Storage in MySQL Database

KEY FEATURES:

~Simulated health data generation using a CSV file.
~Data streaming to five Kafka topics based on data type.
~Kafka consumer module retrieves, processes, and stores data in a MySQL database.
~Efficient real-time data flow leveraging Apache Kafka for message processing.

TECHNOLOGIES USED:
~Python (data generation, Kafka producer & consumer)
~Apache Kafka (message broker for distributed data processing)
~MySQL (relational database for storage)
~Confluent Kafka Python library (Kafka integration)
~Pandas (data handling)

PREREQUISITES:
Apache Kafka installed and running
Python 3.x installed
MySQL Server running on port 3307

POTENTIAL USE CASES:
Real-time health monitoring systems
IoT-based patient tracking
Data-driven medical insights
Remote healthcare solutions
