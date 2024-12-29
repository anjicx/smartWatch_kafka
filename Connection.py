import mysql.connector

# Funkcija za kreiranje konekcije sa MySQL bazom
def create_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",        # Promenite prema konfiguraciji
            password="",        # nema šifre podešeno
            database="healthdata",  # Ime baze
            port=3307
        )
        return conn #vraca obj klase koja je instanca mysql.connector biblioteke 
    except mysql.connector.Error as err:
        print(f"Error connecting to database: {err}")
        return None


# Funkcije za ubacivanje podataka u odgovarajuće tabele
def insert_heart_data(cursor, data):
    query = """
    INSERT INTO heart_data (timestamp, heart_rate, stress_level)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, data)

def insert_blood_pressure_data(cursor, data):
    query = """
    INSERT INTO blood_pressure_data (timestamp, systolic_bp, diastolic_bp)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, data)

def insert_oxygen_data(cursor, data):
    query = """
    INSERT INTO oxygen_data (timestamp, spo2)
    VALUES (%s, %s)
    """
    cursor.execute(query, data)

def insert_activity_data(cursor, data):
    query = """
    INSERT INTO activity_data (timestamp, steps, calories)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, data)

def insert_sleep_data(cursor, data):
    query = """
    INSERT INTO sleep_data (timestamp, sleep_quality)
    VALUES (%s, %s)
    """
    cursor.execute(query, data)
