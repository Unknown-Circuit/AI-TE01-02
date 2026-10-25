from planner_agent import PlannerAgent
from booking_agent import BookingAgent

def run_multi_agent_system():
    print("=== MENGANALISIS PERMINTAAN PEMESANAN (MULTI-AGENT) ===")
    
    planner = PlannerAgent("FlightPlanner")
    booking = BookingAgent("FlightBooker")
    
    user_request = {"origin": "Jakarta", "destination": "Bali", "budget": 1000000}
    
    # Step 1: Planner Agent mencari opsi
    plan = planner.plan_flight(user_request)
    print(f"\n[{planner.name}]: {plan['message']}")
    
    # Step 2: Booking Agent mengeksekusi jika penerbangan ditemukan
    if plan["success"]:
        result = booking.execute_booking(plan["selected_flight"])
        print(f"\n[{booking.name}]: {result['message']}")

if __name__ == "__main__":
    run_multi_agent_system()