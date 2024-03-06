import os
import time
from datetime import datetime
from sys import platform


# Delete old backups?
clear_backups = False
backup_location = "/media/backup"
backup_dirs = ["/etc"]
backup_name_format = "%date%-%backupName%"
date = time.strftime("%Y_%m_%d-%H_%M")
start_time = time.time()

class Logger:
    file = None

    def __init__(self, fileName):
        self.file = open(fileName, "a")

    def log(self, logLevel, message):
        now = str(datetime.now())
        self.file.write("[" + now + "] " + logLevel + ": " + message + " \n")
        print("\n [" + now + "] " + logLevel + ": " + message + " \n")

    def close_file(self): 
        self.file.close()

def os_check():
    if platform.startswith('linux'):
        return True
    else:
        return False

def create_backup_location():
    logger.log("INFO", "Creating backup directory...")
    os.makedirs(backup_location)


def clear_backups():  
    logger.log("INFO", "Cleaning backup directory...")  
    for file in os.listdir(backup_location):
        if os.path.isfile(file):
            os.remove(file)
        elif os.path.isdir(file):
            os.rmdir(file)
        else:
            logger.log("ERROR", file + " can't be deleted.")
    logger.log("SUCCESS", "Successfully deleted old backup files.")

def get_file_name(name):  
    file_name = backup_name_format
    file_name = file_name.replace('%date%', date)
    file_name = file_name.replace('%backupName%', name)

    print(file_name)

    return file_name

def backup():
    logger.log("INFO", "Starting backup for " + str(len(backup_dirs)) + " directories...")
    if len(backup_dirs) == 0:
        logger.log("INFO", "No directories to backup")
    else:
        count = 0
        for directory in backup_dirs:
            backup_file_name = get_file_name('backup_' + str(count + 1)) + '.tar.gz'  
            count += 1
            logger.log("INFO", "Starting backup for " + directory + "...")  
            status = os.system("cd " + backup_location + " && tar -czvf " + backup_file_name + " " + directory)  
            if status == 0:
                logger.log("SUCCESS", "Backup for " + directory + " was successful.")  
            else:
                logger.log("ERROR", "Failed to backup " + directory + ".")  
    logger.log("SUCCESS", "Elapsed time: " + str(time.time() - start_time))


logger = Logger("backup.log")
if os_check():
    if os.path.exists(backup_location):
        if clear_backups:
            clear_backups()
        backup()
    else:
        logger.log("ERROR", "Failed to create backup.")
        logger.log("ERROR", backup_location + " does not exist.")
        create_backup_location()
        backup()

    logger.close_file()
else:
    logger.log("ERROR", "This script is only for Linux.")
    logger.close_file()
