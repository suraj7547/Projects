import random
from datetime import datetime

STATIONS = {
    "City Center": 1.4,
    "Industrial Zone": 2.2,
    "Residential Area": 0.9,
    "Highway Corridor": 1.8,
    "Green Park": 0.6
}

AQI_CATEGORIES = [
    (0, 50, "Good"),
    (51, 100, "Moderate"),
    (101, 150, "Unhealthy for Sensitive Groups"),
    (151, 200, "Unhealthy"),
    (201, 300, "Very Unhealthy"),
    (301, 500, "Hazardous")
]

data_log = []

def get_category(aqi):
    for low, high, category in AQI_CATEGORIES:
        if low <= aqi <= high:
            return category
    return "Out of Range"

def generate_data():
    readings = {}
    for station, factor in STATIONS.items():
        base = random.randint(30, 150)
        aqi = min(int(base * factor), 500)
        readings[station] = aqi
    return readings

def log_data(readings):
    time = datetime.now().strftime("%H:%M:%S")
    for station, aqi in readings.items():
        category = get_category(aqi)
        data_log.append([time, station, aqi, category])

def display(readings):
    print("\n--- Live AQI ---")
    for s, aqi in readings.items():
        print(f"{s}: {aqi} ({get_category(aqi)})")

def analysis():
    if not data_log:
        print("No data available")
        return

    total = 0
    max_aqi = -1
    min_aqi = 999
    worst = best = ""

    for row in data_log:
        aqi = int(row[2])
        total += aqi
        if aqi > max_aqi:
            max_aqi = aqi
            worst = row[1]
        if aqi < min_aqi:
            min_aqi = aqi
            best = row[1]

    avg = total / len(data_log)

    print("\n--- Analysis ---")
    print(f"Average AQI: {avg:.2f}")
    print(f"Worst Location: {worst} ({max_aqi})")
    print(f"Best Location: {best} ({min_aqi})")

def ascii_graph():
    if not data_log:
        print("No data to display")
        return

    print("\n--- AQI Graph (ASCII) ---")
    for row in data_log[-10:]:  # last 10 readings
        aqi = int(row[2])
        bar = "#" * (aqi // 10)  # scale down
        print(f"{row[1][:10]:10} | {bar} ({aqi})")

def search_station():
    name = input("Enter station name: ")
    found = False
    for row in data_log:
        if row[1].lower() == name.lower():
            print(f"Time: {row[0]}, AQI: {row[2]}, Category: {row[3]}")
            found = True
    if not found:
        print("No data found")

def menu():
    while True:
        print("\n1. Generate AQI Data")
        print("2. View Analysis")
        print("3. Show ASCII Graph")
        print("4. Search by Station")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            readings = generate_data()
            log_data(readings)
            display(readings)

        elif choice == "2":
            analysis()

        elif choice == "3":
            ascii_graph()

        elif choice == "4":
            search_station()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()
