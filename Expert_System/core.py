class FlightBookingCore:
    def __init__(self, knowledge_base):
        self.kb = knowledge_base

    def search_flights(self, origin, destination):
        flights = self.kb.get_all_flights()
        matched_flights = [
            f for f in flights 
            if f["origin"].lower() == origin.lower() and f["destination"].lower() == destination.lower()
        ]
        return matched_flights

    def validate_passenger_info(self, name, passport_id):
        if len(name.strip()) > 0 and len(passport_id.strip()) >= 6:
            return True
        return False
