import math

class Date():
    def __init__(self, year, month, day):
        self.__year = year
        self.__month = month
        self.__day = day
        self.__weekday = self.__toWeekday()

    def now():
        pass

    def fromString(s):
        pass

    def __toWeekday(self):
        year = self.__year - (1 if self.__month < 3 else 0)
        c = year // 100
        d = year % 100
        m = (self.__month + 9) % 12 + 1
        d = self.__day
        return (math.floor(2.6 * m + 0.8) + math.floor(c / 4) + math.floor(d / 4) - 2 * c + d) % 7

    def weekday(self):
        return self.__weekday
    
    def day(self, day = None):
        if day:
            self.__day = day
            self.__weekday = self.__toWeekday()
        else:
            return self.__day
