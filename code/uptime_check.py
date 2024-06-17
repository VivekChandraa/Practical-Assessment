"""
Application Health Checker:
Please write a script that can check the uptime of an application and
determine if it is functioning correctly or not. The script must accurately
assess the application's status by checking HTTP status codes. It should be
able to detect if the application is 'up', meaning it is functioning correctly, or
'down', indicating that it is unavailable or not responding."""

import requests
import logging

# Configuration
URL = "https://www.google.co.in/"  # application URL
def log_message(message):
    print(message)
    logging.info(message)

def check_application_status():
    try:
        response = requests.get(URL, timeout=10)
        if 200 <= response.status_code < 300:
            log_message(f"Application is UP. Status code: {response.status_code}")
        else:
            log_message(f"Application is DOWN. Status code: {response.status_code}")
    except requests.RequestException as e:
        log_message(f"Application is DOWN. Error: {e}")

check_application_status()
