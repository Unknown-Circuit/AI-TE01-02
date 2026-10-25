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


## Source / Referensi

- Repositori Asal: [tzolov/playground-flight-booking](https://github.com/tzolov/playground-flight-booking).
- Penulis / Kontributor Utama: **Tsvetan Zolov**.
- Snapshot: [commit terbaru](https://github.com/tzolov/playground-flight-booking/tree/main).
- Source Inti Agen & Tools: Modul sistem pemesanan penerbangan dan pencarian rute berbasis AI Agent / Multi-Agent Framework.
- Lisensi: Terikat pada lisensi asli repositori upstream (disertakan di `LICENSE`).
- Penyesuaian Struktur:
  - Kode dan modul dari repositori asli telah direstrukturisasi ke dalam folder modul terpisah (`Flight_Booking_Agent`, `Multi_Agent_System`, dan `Flight_Search_Algorithm`) agar sesuai dengan standar format proyek `PT-Mencari-Bakat/AI-TE01-03`.
  - Penambahan antarmuka `app.py`, skrip eksekusi `main.py`, konfigurasi dependensi `requirements.txt`, serta dokumentasi `README.md` berbahasa Indonesia untuk setiap modul.
  - Dokumentasi asli disimpan/disesuaikan dalam file `project_report_Version1.md` dan `README.md`.
   python app.py
   ```
