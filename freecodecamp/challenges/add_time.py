
# First seprate hour and minutes and meredian -done
# convert them into 24 hour time - done
# add hours and minutes - done
# find which day is current - done
# convert time into standard time
# output the result

weekdays = {
  'monday': 0,
  'tuesday': 1,
  'wednesday': 2,
  'thursday': 3,
  'friday': 4,
  'saturday': 5,
  'sunday': 6
}

daysweek = {
  0: 'monday',
  1: 'tuesday',
  2: 'wednesday',
  3: 'thursday',
  4: 'friday',
  5: 'saturday',
  6: 'sunday'
}

class Time:
  hours = 0
  minutes = 0
  start_day = None
  
  def __init__(self, time, day=None):
    hours_minutes, mer = tuple(time.split())
    hours, minutes = tuple(hours_minutes.split(':'))
    hours, minutes = int(hours), int(minutes) 
    if mer.lower() == 'am':
      if hours == 12: hours = 0
    else:
      if hours != 12: hours += 12
    self.hours = hours
    self.minutes = minutes
    if day: self.start_day = day.lower()
      
  def add_hours_and_minutes(self, hours_minutes):
    hours, minutes = tuple(hours_minutes.split(':'))
    hours, minutes = int(hours), int(minutes)
    self.hours += hours
    self.minutes += minutes
    self.hours += self.minutes // 60
    self.minutes = self.minutes % 60
  
  def day_number(self):
    result = self.hours // 24
    if result == 0: return ''
    if result == 1: return ' (next day)'
    return ' ({} days later)'.format(result)
  
  def current_time(self):
    hours, minutes = self.hours % 24, self.minutes
    new_meridian = 'AM'
    if hours >= 12: new_meridian = 'PM'
    if hours == 0: hours = 12
    if hours > 12: hours -= 12
    if minutes < 10: minutes = '0' + str(minutes)
    return '{}:{} {}'.format(hours, minutes, new_meridian)
  
  def current_day(self):
    if self.start_day:
      days = self.hours // 24
      return daysweek[(weekdays[self.start_day] + days) % 7].capitalize()
    return

  def display_result(self):
    if self.current_day():
      return '{}, {}{}'.format(self.current_time(), self.current_day(), self.day_number())
    else:
      return '{}{}'.format(self.current_time(), self.day_number())
    


def add_time(start, duration):
  t = Time(start)
  t.add_hours_and_minutes(duration)
  return t.display_result()

if __name__ == '__main__':
  print(add_time('3:30 PM', '2:12'))