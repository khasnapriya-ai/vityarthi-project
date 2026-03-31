# vityarthi-project
# NAME - KANKALA HASNA PRIYA
# REGISTRATION NUMBER - 25BAI10583
⏰ Python Alarm Clock Project
1. Project Overview
The Python Alarm Clock is a simple yet functional console-based alarm system. It allows users to set an alarm time, monitors the system clock in real-time, and alerts the user when the alarm time is reached.
Key Features:
•	Set a one-time alarm in HH:MM: SS format
•	Continuous time monitoring with real-time display
•	Plays an alarm sound to notify the user
•	Simple and lightweight Python implementation
•	Can be extended to include GUI, multiple alarms, or snooze functionality
________________________________________
2. Purpose and Learning Outcomes
This project is ideal for beginners learning Python. By building it, you will learn:
•	Handling date and time in Python using datetime
•	Implementing real-time loops with the time module
•	Playing audio notifications using play sound
•	Basic user interaction and input handling
•	Structuring Python scripts for a small real-world project
This project also introduces concepts of event-driven programming, where actions are triggered based on system events (alarm time matching current time).
________________________________________
3. Tools and Technologies
Component	Description
Python 3.x	Programming language used for implementation
datetime (built-in)	Handles current system time and formatting
time (built-in)	Used for creating delays (1-second intervals)
Play sound	Plays audio files for alarm notifications
Optional GUI	Tkinter or PyQt can be added for future versions
________________________________________
4. Prerequisites
Before running this project, ensure the following:
1.	Python 3.x is installed:
Download Python
2.	pip is installed (comes with Python 3.x)
3.	(Optional) A virtual environment to manage dependencies
________________________________________
5. Step-by-Step Setup Instructions
Step 1: Clone the Repository
git clone <your-repo-url>
cd python-alarm-clock
Step 2: (Optional) Create a Virtual Environment
# Create environment
python -m venv env

# Activate (Windows)
env\Scripts\activate

# Activate (Linux/Mac)
source env/bin/activate
Step 3: Install Dependencies
pip install play sound
Note: datetime and time are built-in modules and don’t need installation.
Step 4: Add Alarm Sound File
Place an audio file (alarm.mp3 or .wav) in the project folder.
Modify the code if you are using a different file name:
Play sound("alarm.mp3")
Step 5: Run the Program
python alarm_clock.py
•	Enter alarm time in HH:MM: SS format when prompted
•	Wait for the program to trigger the alarm at the set time
Step 6: Deactivate Virtual Environment (Optional)
deactivate
________________________________________
6. Code Explanation
1.	Importing Libraries
import time
from datetime import datetime
from play sound import play sound
2.	User Input
Alarm _time = input("Enter alarm time (HH:MM:SS): ")
3.	Monitoring Loop
while True:
    current _time = datetime. now().strf time("%H:%M:%S")
    print ("Current Time:", current _time)
    if current _time == alarm _time:
        print("Wake up! Alarm ringing!")
        play sound("alarm.mp3")
        break
    time. sleep(1)
•	The program continuously checks current system time
•	Plays sound when time matches
________________________________________
7. Output
Enter alarm time (HH:MM:SS): 07:30:00
Alarm set for: 07:30:00
Current Time: 07:29:58
Current Time: 07:29:59
Current Time: 07:30:00
Wake up! Alarm ringing!
________________________________________
8. Advantages
•	Lightweight and simple implementation
•	Cross-platform compatibility (Windows, Linux, Mac)
•	Easy to extend with GUI and advanced features
•	Good learning project for beginners
________________________________________
9. Limitations
•	Only supports single alarm in basic version
•	Requires exact match of system time
•	Needs audio file to be present for sound alerts
•	No GUI in basic console version
________________________________________
10. Future Enhancements
•	Graphical User Interface (Tkinter / PyQt)
•	Multiple alarms with names and descriptions
•	Snooze functionality
•	Custom alarm sounds
•	Recurring alarms (daily, weekly)
•	Voice alerts using text-to-speech
________________________________________
11. Troubleshooting
•	playsound error: Ensure alarm.mp3 exists in the project folder and is not corrupted
•	Wrong time format: Always enter alarm in HH:MM:SS 24-hour format
•	Virtual environment not activating: Check your Python installation and path variables
________________________________________
12. Best Practices
•	Use a virtual environment to manage dependencies
•	Keep alarm audio files in the same folder as the script
•	For GUI enhancements, separate code into modules for better structure
________________________________________
13. Project Folder Structure
python-alarm-clock/
│
├─ alarm_clock.py        # Main Python script
├─ alarm.mp3             # Audio file for alarm
├─ README.md             # Project documentation
├─ requirements.txt      # Dependencies file
└─ .gitignore            # Git ignore file
  
14. Requirements File (requirements.txt)
Play sound==1.2.2

