class Time:
    #previous method definitions here...
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds
    
    def convertToSeconds(self):
        minutes = self.hours * 60 + self.minutes
        seconds = minutes * 60 + self.seconds
        return seconds
    
    def increment(self, seconds):       #self here talks to parameter time
        self.seconds = seconds + self.seconds

        while self.seconds >= 60:
            self.seconds = self.seconds - 60
            self.minutes = self.minutes + 1

        while self.minutes >= 60:
            self.minutes = self.minutes - 60
            self.hours = self.hours + 1
            
class Point:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
        
    def __sub__(self, other):
        return Point(other.x-self.x, other.y-self.y)
        
    def reverse(self):
        self.x , self.y = self.y, self.x
    
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'