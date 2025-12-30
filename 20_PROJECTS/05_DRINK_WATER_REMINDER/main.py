import time
"""
Drink Water Reminder Application
This module implements a simple reminder system that notifies the user to drink water
at regular intervals. It displays both console messages and system notifications to
encourage the user to stay hydrated and take breaks.
The application runs in an infinite loop, sending reminders every hour.
Dependencies:
    - plyer: For cross-platform system notifications
    - time: For managing time intervals between reminders
Usage:
    Run the script directly to start receiving water reminders:
    python main.py
Author: Rayan
Created: 2024
"""
from plyer import notification

while True:
    print("Reminder: Take a short break and stretch!")
    notification.notify(title = "please drink some water",
                        message = "you need to stay hyderated!")
    time.sleep(60 * 60)  # Wait 1 hour before next reminder