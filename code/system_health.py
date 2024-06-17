"""
1. System Health Monitoring Script:
Develop a script that monitors the health of a Linux system. It should check
CPU usage, memory usage, disk space, and running processes. If any of
these metrics exceed predefined thresholds (e.g., CPU usage > 80%), the
script should send an alert to the console or a log file.
"""


import psutil
import logging

# Define thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 90
PROCESS_THRESHOLD = 250  # Example threshold for the number of running processes

def log_message(message):
    print(message)
    logging.info(message)

def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_message(f"ALERT: High CPU usage detected: {cpu_usage}%")
    else:
        log_message(f"CPU usage is normal: {cpu_usage}%")

def check_memory():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        log_message(f"ALERT: High memory usage detected: {memory_usage}%")
    else:
        log_message(f"Memory usage is normal: {memory_usage}%")

def check_disk():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        log_message(f"ALERT: High disk usage detected: {disk_usage}%")
    else:
        log_message(f"Disk usage is normal: {disk_usage}%")

def check_processes():
    process_count = len(psutil.pids())
    if process_count > PROCESS_THRESHOLD:
        log_message(f"ALERT: High number of running processes detected: {process_count}")
    else:
        log_message(f"Number of running processes is normal: {process_count}")

def check_system_health():
    log_message("Starting system health check...")
    check_cpu()
    check_memory()
    check_disk()
    check_processes()
    log_message("System health check completed.")

check_system_health()
