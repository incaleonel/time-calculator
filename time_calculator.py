def add_time(start, duration, day=''):

    class Time:
        weekdays = ['Sunday','Monday','tuesday','Wednesday','Thursday','Friday','saturDay','']
        def __init__(self, horary):
            
            timeSplit = horary.split()
            self.hour = int(timeSplit[0].split(':')[0])
            self.minute = int(timeSplit[0].split(':')[1])
            self.ampm = False if len(timeSplit) > 1 and timeSplit[1] == 'AM' else True #False -> AM /// True -> PM or void
            self.count = 0
            self.weekday = 0
            self.message = ''
            self.time = horary
            
        def addTime(self, addHour, addMin, day = ''):
            self.weekday = self.weekdays.index(day)
            self.minute += addMin
            if self.minute > 59 :
                addHour += int(self.minute/60)
                self.minute = self.minute % 60
            self.hour = 0 if self.hour == 12 else self.hour
            self.hour += addHour
            if self.hour >= 12:
                self.count += int(self.hour/12)
                self.hour = self.hour % 12
            
            if self.ampm:
                self.weekday = (self.weekday + int((self.count + 1)/2)) % 7
                self.message = ' (next day)' if self.count == 1 or self.count == 2 else ''
                if self.count > 2:
                    self.message = ' (' + str(int((self.count + 1)/2)) + ' days later)'
            else :
                self.weekday = (self.weekday + int((self.count)/2)) % 7
                self.message = ' (next day)' if self.count == 2 or self.count == 3 else ''
                if self.count > 3:
                    self.message = ' (' + str(int(self.count/2)) + ' days later)'
            self.ampm = not(self.ampm) if self.count % 2 else self.ampm       
            strMin = str(self.minute) if len(str(self.minute)) > 1 else '0' + str(self.minute)
            self.time =  str(self.hour) if self.hour else '12' 
            self.time += ':' + strMin + ' '
            self.time += 'PM' if self.ampm else 'AM'
            self.time += ', ' + self.weekdays[self.weekday] if self.weekdays.index(day) != 7 else ''
            self.time += self.message
        
    s = Time(start)
    d = Time(duration)
    s.addTime(d.hour, d.minute,day)
    new_time = s.time

    return new_time