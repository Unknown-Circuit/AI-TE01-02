class PlannerAgent:
    def __init__(self, name="PlannerAgent"):
        self.name = name

    def plan_flight(self, request):
        origin = request.get("origin")
        destination = request.get("destination")
        budget = request.get("budget", 0)

        print(f"[{self.name}] Mencari rute optimal dari {origin} ke {destination} dengan anggaran Rp {budget:,}...")

        # Simulasi analisis perencana
        if budget >= 750000:
            flight = {"id": "FL002", "airline": "AirAsia", "price": 750000}
            return {
                "success": True,
                "selected_flight": flight,
                "message": f"Ditemukan penerbangan cocok dengan {flight['airline']} seharga Rp {flight['price']:,}."
            }
        else:
            return {
                "success": False,
                "selected_flight": None,
                "message": "Tidak ada penerbangan yang sesuai dengan anggaran yang ditentukan."
            }