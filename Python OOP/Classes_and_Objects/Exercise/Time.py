import datetime

class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, new_hours, new_minutes, new_seconds):
        self.hours = new_hours
        self.minutes = new_minutes
        self.seconds = new_seconds


    def get_time(self):
        return str(datetime.time(self.hours, self.minutes, self.seconds))

    def next_second(self):
        if self.seconds + 1 < Time.max_seconds:
            self.seconds += 1
            return str(datetime.time(self.hours, self.minutes, self.seconds))
        else:
            self.seconds = 00
            if self.minutes + 1 < Time.max_minutes:
                self.minutes += 1
                return str(datetime.time(self.hours, self.minutes, self.seconds))
            else:
                self.minutes = 00
                if self.hours + 1 < Time.max_hours:
                    self.hours += 1
                    return str(datetime.time(self.hours, self.minutes, self.seconds))
                else:
                    self.hours = 0
                    return str(datetime.time(self.hours, self.minutes, self.seconds))


time = Time(23, 59, 59)
print(time.next_second())

