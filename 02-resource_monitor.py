
from datetime import datetime
import psutil

def get_system_resources():
    try:
        psutil.cpu_percent(interval=1, percpu=True)
        cpu_percent = psutil.cpu_percent()
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

  
def print_system_resources():
    data = get_system_resources()
    if data:
        print("\n", data)
    else:
        print("Failed to retrieve system resources.")
        
        
print_system_resources()
