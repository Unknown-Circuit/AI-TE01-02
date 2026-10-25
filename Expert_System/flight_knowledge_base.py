class FlightKnowledgeBase:
    def __init__(self):
        self._flights = [
            {"id": "FL001", "origin": "Jakarta", "destination": "Bali", "airline": "Garuda Indonesia", "price": 1200000, "duration": "1j 50m"},
            {"id": "FL002", "origin": "Jakarta", "destination": "Bali", "airline": "AirAsia", "price": 750000, "duration": "2j 00m"},
            {"id": "FL003", "origin": "Jakarta", "destination": "Surabaya", "airline": "Lion Air", "price": 600000, "duration": "1j 30m"},
            {"id": "FL004", "origin": "Surabaya", "destination": "Bali", "airline": "Citilink", "price": 450000, "duration": "0j 50m"},
        ]

    def get_all_flights(self):
        return self._flights