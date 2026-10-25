class BookingAgent:
    def __init__(self, name="BookingAgent"):
        self.name = name

    def execute_booking(self, flight_info):
        print(f"[{self.name}] Memproses transaksi pemesanan untuk penerbangan ID: {flight_info['id']}...")
        return {
            "booking_id": "BK-20261026-99",
            "status": "CONFIRMED",
            "message": f"Tiket berhasil dipesan! Kode Booking: BK-20261026-99 ({flight_info['airline']})."
        }