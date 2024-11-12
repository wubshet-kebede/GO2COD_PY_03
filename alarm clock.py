import datetime
import time
import playsound  # Install this library using 'pip install playsound'

def set_alarm():
    """Sets the alarm time and plays a sound when the time is reached."""

    while True:
        alarm_hour = int(input("Enter the alarm hour (0-23): "))
        alarm_minute = int(input("Enter the alarm minute (0-59): "))

        if 0 <= alarm_hour <= 23 and 0 <= alarm_minute <= 59:
            break
        else:
            print("Invalid time. Please enter valid hours and minutes.")

    alarm_time = datetime.datetime(
        datetime.datetime.now().year,
        datetime.datetime.now().month,
        datetime.datetime.now().day,
        alarm_hour,
        alarm_minute,
        0
    )

    print(f"Alarm set for: {alarm_time.strftime('%H:%M')}")

    while True:
        now = datetime.datetime.now()
        if now >= alarm_time:
            print("Wake up!")
            playsound.playsound('alarm_sound.mp3')  # Replace with your desired alarm sound file
            break
        time.sleep(1)  # Check every second


if __name__ == "__main__":
    set_alarm()

