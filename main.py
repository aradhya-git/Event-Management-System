
from api_interaction import api_call
from event import Event
from event_database import EventDatabase

if __name__ == "__main__":

  event_database = EventDatabase()

  event_data = api_call("URL", {start_date:"",End_date:""}) #Returns a list of events assuming returns a list of new events

  
  event_database.add_event(event['Event']) # sends list of new events from API Call

  event_name = "eventx"
  event = event_database.get_event(event_name) #name of event and event date

  event_obj = Event(event[0], event[1]) # we can have different name for event name and event date
                                        # Here I used event name and date from get event function
  days_until_event = event_obj.days_until_event()
  print("No of days for the event eventx: ", days_until_event)

  upcoming_events = event_database.upcoming_events()
  print("Total events in next 30 days", upcoming_events)
