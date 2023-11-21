from datetime import datetime
import time


class DownloadDelay:

    def __init__(self, current_time, target_time):
        self.current_time = current_time
        self.target_time = target_time

    # formats the time given by user from HH:MM into a datetime object
    def text_to_datetime(self, time):
        if time is not None:
            time_object = datetime.strptime(time, '%H:%M')  # formats time, this will go into class later
            return time_object
        else:
            return None

    def schedule_delay(self):
        print(self.current_time)
        print(self.target_time)
        if self.current_time < self.target_time:
            hourToWait = abs(self.target_time.hour - self.current_time.hour)
            minsToWait = abs(self.target_time.minute - self.current_time.minute)
            secsToWait = abs(self.target_time.second - self.current_time.second)
            totalWaitTime = round((hourToWait * 60) + minsToWait + (secsToWait / 60))
            print("Program delayed by " + str(totalWaitTime) + " minutes")
            time.sleep(totalWaitTime)
        else:
            # cont here
