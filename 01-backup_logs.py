import os
import time
from datetime import datetime
import platform

backup_directory = "./media/backup"
backup_dirs = ["/etc"]
backup_name_format = "%Y-%m-%d__%H:%M-backupName.tar.gz"
start_time = time.time()

def os_check():
    return platform.system() == 'Linux'

def create_backup_directory():
    os.makedirs(backup_directory, exist_ok=True)

def get_file_name(name):
    return datetime.now().strftime(backup_name_format).replace('backupName', name)

def backup():
    if not backup_dirs:
        print("No directories to backup")
    else:
        for count, directory in enumerate(backup_dirs, start=1):
            backup_file_name = get_file_name(f'backup_{count}')
            status = os.system(f"cd {backup_directory} && tar -czvf {backup_file_name} {directory}")
            if status == 0:
                print(f"Backup for {directory} was successful.")
            else:
                print(f"Failed to backup {directory}.")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")

def main():
    if os_check():
        if os.path.exists(backup_directory):
            backup()
        else:
            print(f"{backup_directory} does not exist.")
            create_backup_directory()
            backup()
    else:
        print("ERROR", "This script is only for Linux.")
    print("INFO", "Script execution finished.")

if __name__ == "__main__":
    main()
