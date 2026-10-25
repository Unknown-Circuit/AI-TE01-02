# AI-TE01-02

# Playground Flight Booking AI System

Sistem kecerdasan buatan berbasis Python untuk pencarian, perencanaan, dan pemesanan tiket pesawat menggunakan pendekatan **Expert System**, **Multi-Agent System**, dan **Search Algorithm**.

---

## 📁 Struktur Repositori

```text
.
├── Flight_Booking_Agent/
│   ├── README.md
│   ├── app.py
│   ├── flight_booking_core.py
│   ├── flight_knowledge_base.py
│   ├── project_report_Version1.md
│   └── requirements.txt
│
├── Multi_Agent_Flight_System/
│   ├── README.md
│   ├── booking_agent.py
│   ├── main.py
│   └── planner_agent.py
│
├── Flight_Search_Algorithm/
│   ├── README.md
│   ├── astar_flight_search.py
│   ├── bfs_flight_search.py
│   ├── dfs_flight_search.py
│   ├── flight_graph_data.py
│   └── requirements.txt
│
└── README.md
```

---

## 🚀 Ringkasan Modul

### 1. `Flight_Booking_Agent/`
Modul sistem pakar (*Expert System*) dan antarmuka aplikasi pemesanan tiket penerbangan secara kontekstual berbasis aturan (*rule-based*).

### 2. `Multi_Agent_Flight_System/`
Sistem kolaborasi multi-agen di mana agen perencana (*planner agent*) dan agen pemesan (*booking agent*) berkoordinasi secara otomatis untuk menyelesaikan transaksi penerbangan.

### 3. `Flight_Search_Algorithm/`
Implementasi berbagai algoritma pencarian jalur (*Search Algorithms*) seperti BFS, DFS, dan A* untuk menemukan rute penerbangan optimal (transit terhitung, harga termurah, durasi tercepat).

---

## 🛠️ Cara Penggunaan

1. Clone repositori ini:
   ```bash
   git clone https://github.com/username/playground-flight-booking.git
   cd playground-flight-booking
   ```

2. Masuk ke modul yang ingin dijalankan dan install dependensi:
   ```bash
   cd Flight_Booking_Agent
   pip install -r requirements.txt
   python app.py
   ```
