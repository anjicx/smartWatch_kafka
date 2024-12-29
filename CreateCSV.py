
import random  # Generisanje nasumičnih brojeva
from datetime import datetime, timedelta  # Rad sa datumima i vremenom
import pandas as pd  # Biblioteka za rad s tabelama (DataFrame)


# Definicija kolona za tabelu (CSV fajl)
columns = [
    "Timestamp", "Heart Rate (BPM)", "Systolic BP", "Diastolic BP",
    "SpO2 (%)", "Steps", "Calories Burned", "Sleep Quality (0-100)", "Stress Level (0-100)"
]

# Lista koja će čuvati sve generisane podatke
data = []
# Početno vreme simulacije: ponoć 24. novembra 2024.
start_time = datetime(2024, 11, 24, 0, 0)
# Ukupan broj zapisa (svaki zapis predstavlja podatke za jedan sat)
num_records = 24
# Generisanje podataka
for i in range(num_records):
    # Izračunavanje vremena za trenutni zapis
    timestamp = start_time + timedelta(hours=i)
    # Nasumično generisanje podataka za zdravstvene parametre
    heart_rate = random.randint(60, 100)  # Srčani ritam (u BPM)
    systolic_bp = random.randint(110, 130)  # Gornji pritisak
    diastolic_bp = random.randint(70, 85)  # Donji pritisak
    spo2 = random.randint(95, 100)  # Nivo kiseonika u krvi (%)
    steps = random.randint(0, 500) if i < 7 else random.randint(500, 2000)  # Manje koraka pre 7h (osoba spava)
    sleep_quality = random.randint(0, 100) if i < 7 else 0  # Kvalitet sna (pre 7h viši, posle 0)
    stress_level = random.randint(10, 70)  # Nivo stresa (u %)
    calories = random.uniform(50, 150)  # Sagorene kalorije (decimalni broj)
    # Dodavanje generisanih podataka u listu
    data.append([
        timestamp,  # Automatski se konvertuje u ISO string format
        heart_rate, systolic_bp, diastolic_bp, spo2,
        steps, round(calories, 2), sleep_quality, stress_level
    ])

# Kreiranje DataFrame tabele pomoću pandas biblioteke
df = pd.DataFrame(data, columns=columns)

# Definisanje putanje za snimanje CSV fajla
file_path = "C:\\python\\simulated_health_data_minute.csv"

# Snimanje DataFrame-a u CSV fajl
df.to_csv(file_path, index=False)  # index=False sprečava automatsko numerisanje redova

#filepath->za vracanje mesta gde je sacuvan csv fajl(da proverimo gde je sacuvano)