# Graf Keterhubungan Bandara beserta Biaya (Cost dalam Ribuan IDR)
FLIGHT_GRAPH = {
    'Jakarta': {'Surabaya': 600, 'Yogyakarta': 450, 'Singapore': 1100},
    'Surabaya': {'Bali': 450, 'Lombok': 550},
    'Yogyakarta': {'Surabaya': 350, 'Bali': 800},
    'Singapore': {'Bali': 1300},
    'Bali': {},
    'Lombok': {}
}