

from datetime import date

class EventDatabase:

  def __init__(self):
    self.events = {}

  def add_event(self, event_list):

    for i in event_list:

      self.events['Event'].append(i) # Event list is list of dictionaries with format {name: date}

  def get_event(self, event_name):

    for i in self.events['Event']:
      for event in i.keys():
        if event == event_name:
          return [event, self.events['Event'][event]] #returns name of the event and event date
    return "Event not present"

  def upcoming_events(self):
    today = date.today()
    upcoming_events = []

    for i in self.events['Event']:
      for event in i.keys():
        event_date = self.events['Event'][event]

        if event_date >= today and event_date <= (today + 30):
          upcoming_events.append(event)

    return upcoming_events # returns a list of events in next 30 days
