import os
import psutil
from datetime import datetime

LOGS_DIRECTORY = "./logs"
LOGS_NAME_FORMAT = "%Y-%m-%d__%H:%M-resources.log"

def get_system_resources():
    try:
        cpu_percent = psutil.cpu_percent(interval=1)
        memory_percent = psutil.virtual_memory().percent
        disk_percent = psutil.disk_usage("/").percent
        timestamp = datetime.now().isoformat()
        data = {
            "cpu": cpu_percent,
            "memory": memory_percent,
            "disk": disk_percent,
            "timestamp": timestamp
        }
        return data
    except psutil.Error as e:
        print(f"Error occurred while retrieving system resources: {e}")
        return None

def print_system_resources(data):
    if data:
        print("\n", data)
    else:
        print("Failed to retrieve system resources.")

def check_and_create_logs_directory():
    os.makedirs(LOGS_DIRECTORY, exist_ok=True)

def get_logs_name():
    return datetime.now().strftime(LOGS_NAME_FORMAT)

def store_data_logs(data):
    try:
        check_and_create_logs_directory()
        filename = get_logs_name()
        filepath = os.path.join(LOGS_DIRECTORY, filename)

        with open(filepath, "a") as f:
            f.write(
                f"{data['timestamp']}, CPU: {data['cpu']}%, Memory: {data['memory']}%, Disk: {data['disk']}%\n")
    except Exception as e:
        print(f"Error occurred while storing data logs: {e}")

def run():
    data = get_system_resources()
    if data:
        store_data_logs(data)
        print_system_resources(data)

if __name__ == "__main__":
    run()
