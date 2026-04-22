import csv
from datetime import datetime

def log_event(event_type):
    with open("logs/events.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), event_type])
