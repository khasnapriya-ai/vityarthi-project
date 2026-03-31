
import time
from datetime import datetime
import os

# Function to set alarm
def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")

    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"Current Time: {current_time}", end="\r")

        if current_time == alarm_time:
            print("\n⏰ Wake up! Alarm ringing!")

            # Beep sound (works on Windows)
            try:
                import winsound
                winsound.Beep(1000, 1000)
            except:
                # For Linux / Mac
                os.system("echo '\a'")
            
            break

        time.sleep(1)

# Take input from user
alarm_time = input("Enter alarm time (HH:MM:SS): ")

set_alarm(alarm_time)