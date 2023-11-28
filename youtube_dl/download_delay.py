from datetime import datetime, timedelta
import time


class DownloadDelay:

    def __init__(self, current_time, target_time):
        self.current_time = current_time
        self.target_time = target_time

    # formats the time given by user from HH:MM into a datetime object
    def text_to_time(self, time):
        if time is not None:
            time_object = datetime.strptime(time, '%H:%M')
            return time_object.time()
        else:
            return None

    # calculates total wait time between the times given in the 24hr time format
    def get_total_wait_time(self, time1, time2):

        if time1 < time2:
            hoursToWait = abs(time2.hour - time1.hour)
            minsToWait = abs(time2.minute - time1.minute)
            secsToWait = abs(time2.second - time1.second)

        # if target time is less than current time, target is assumed to be for the next day
        elif time1 > time2:
            hoursToWait = abs((time2.hour + 24) - time1.hour)
            minsToWait = abs(time2.minute - time1.minute)
            secsToWait = abs(time2.second - time1.second)

        else:
            print("Time given is the same as the as current time, no delay will be applied")
            hoursToWait = 0
            minsToWait = 0
            secsToWait = 0

        totalWaitTime = round((hoursToWait * 60) + minsToWait + (secsToWait / 60))
        return totalWaitTime
    
    def schedule_delay(self):
        totalWaitTime = self.get_total_wait_time(self.current_time, self.target_time)
        print("The download has been scheduled, video download will resume at " + str(self.target_time))
        print("Please leave the program running")
        time.sleep(totalWaitTime)