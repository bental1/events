

class MockEvent(object):
    def __init__(self, event_id, name, participants, location, date, creation_time):
        self.id = event_id
        self.name = name
        self.participants = participants
        self.location = location
        self.date = date
        self.creation_time = creation_time


class MockEvents(object):
    def all(self):
        return [MockEvent(1,1,1,1,1,1), MockEvent(2,2,2,2,2,2)]

