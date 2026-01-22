class MeetingRoom:
    def __init__(self, name):
        self.name = name
        self.slots_booked = []

    def is_available(self, slot):
        if slot in self.slots_booked:
            return False
        return True

    def book_room(self, slot):
        if self.is_available(slot):
            self.slots_booked.append(slot)
            return True
        
        return False

    # Method overriding - Polymorphism
    def price_per_hour(self):
        return 0