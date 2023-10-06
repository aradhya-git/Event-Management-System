# Event-Management-System
 
Imagine you're developing a basic event management system. The system keeps track of various events and their dates. Here's what you need to implement:
 
API Interaction Module(api_interaction.py): 

Request-sample = {start_date:’’
End_date:””
}

Response-sample = {
Event : [
{event1: date}, {event2: date\}
]
}


### API Interaction Module(api_interaction.py): 

fetch_event_data : Makes an API call to the given API Endpoint to fetch event data. Returns a list of events, where each event is represented as a dictionary with a name and a date (date format: 'YYYY-MM-DD').


### Event Module (event.py):

An `Event` class which has two attributes: `name` (name of the event) and `date` (date of the event in the format 'YYYY-MM-DD').
A method `days_until_event` which returns the number of days left until the event from today's date.


### Event Database Module (event_database.py):

Use a dictionary to simulate a database of events where the key is the event's name and the value is an instance of the `Event` class. for example {"test_event_1": event_object}
A method `add_event` which adds an event to the database.
A method `get_event` which returns an event from the database based on the event's name.
A method `upcoming_events` which returns a list of events that are coming in the next 30 day.
 
### Main Module (main.py):

Import the required modules.
Create a few events and add them to the database.
Print the number of days left for an event.
Print the upcoming events for the next 30 days.
