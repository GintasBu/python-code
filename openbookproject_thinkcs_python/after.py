class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds

def time_seconds(time):
    seconds=time.seconds
    secm=time.minutes*60
    sech=time.hours*3600
    return seconds+secm+sech
    
def after(time1, time2):
    t1=time_seconds(time1)
    t2=time_seconds(time2)
    if time1>time2:
        return True
    else: 
        return False

        
def increment(time, seconds):
    time.seconds = time.seconds + seconds

    if time.seconds >= 60:
        time.seconds = time.seconds - 60
        time.minutes = time.minutes + 1

    if time.minutes >= 60:
        time.minutes = time.minutes - 60
        time.hours = time.hours + 1
    return time
        
def increment_noloop(time):
    t=time_seconds(time)
    hours=t/3600
    t=t-hours*3600
    minutes=t/60
    seconds=t-minutes*60
    time2=Time()
    time2.hours=hours
    time2.minutes=minutes
    time2.seconds=seconds
    return time2
    
def print_time(time):
    print '%s:%s:%s' % (str(time.hours), str(time.minutes), str(time.seconds))