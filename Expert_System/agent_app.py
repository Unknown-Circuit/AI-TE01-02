import sys
from core import FlightBookingCore
from flight_knowledge_base import FlightKnowledgeBase

def main():
    print("=" * 50)
    print(" Selamat Datang di Flight Booking Agent (Expert System)")
    print("=" * 50)
    
    kb = FlightKnowledgeBase()
    core = FlightBookingCore(kb)
    
    origin = input("Masukkan Kota / Bandara Asal (contoh: Jakarta): ")
    destination = input("Masukkan Kota / Bandara Tujuan (contoh: Bali): ")
    
    results = core.search_flights(origin, destination)
    
    if results:
        print(f"\n[+] Ditemukan {len(results)} penerbangan:")
        for idx, flight in enumerate(results, 1):
            print(f"  {idx}. {flight['airline']} - Rp {flight['price']:,} ({flight['duration']})")
    else:
        print("\n[-] Penerbangan tidak ditemukan untuk rute tersebut.")

if __name__ == "__main__":
    main()
