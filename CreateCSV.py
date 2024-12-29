
import random  
from datetime import datetime, timedelta 
import pandas as pd  

columns = [
    "Timestamp", "Heart Rate (BPM)", "Systolic BP", "Diastolic BP",
    "SpO2 (%)", "Steps", "Calories Burned", "Sleep Quality (0-100)", "Stress Level (0-100)"
]

data = []
start_time = datetime(2024, 11, 24, 0, 0)
num_records = 24
for i in range(num_records):
    timestamp = start_time + timedelta(hours=i)
    heart_rate = random.randint(60, 100)  
    systolic_bp = random.randint(110, 130)  
    diastolic_bp = random.randint(70, 85)  
    spo2 = random.randint(95, 100)  
    steps = random.randint(0, 500) if i < 7 else random.randint(500, 2000)  
    sleep_quality = random.randint(0, 100) if i < 7 else 0  
    stress_level = random.randint(10, 70)  
    calories = random.uniform(50, 150)  
    data.append([
        timestamp, 
        heart_rate, systolic_bp, diastolic_bp, spo2,
        steps, round(calories, 2), sleep_quality, stress_level
    ])

df = pd.DataFrame(data, columns=columns)
file_path = "C:\\python\\simulated_health_data_minute.csv"

df.to_csv(file_path, index=False) 

