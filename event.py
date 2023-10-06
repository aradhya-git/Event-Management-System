from datetime import date

class Event:

  def __init__(self, name, date):
    self.name_event = name
    self.date_event = date

  def days_until_event(self):

    today = date.today()
    return (self.date_event - today).days
