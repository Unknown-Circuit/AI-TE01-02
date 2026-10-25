# Flight Search Algorithm

Modul pencarian jalur (*route finding*) penerbangan menggunakan algoritma grafik klasik seperti BFS, DFS, dan A*.

## 📄 Berkas dalam Folder

- **`flight_graph_data.py`**: Matriks/graf keterhubungan antar-bandara dan bobot biaya/jarak.
- **`bfs_flight_search.py`**: Algoritma *Breadth-First Search* (mencari rute transit tersingkat).
- **`dfs_flight_search.py`**: Algoritma *Depth-First Search*.
- **`astar_flight_search.py`**: Algoritma *A* Search* (mencari jalur tercepat/termurah berbasis heurisitk).
- **`requirements.txt`**: Pustaka pendukung graf.

## 🚀 Jalankan Pencarian

```bash
python astar_flight_search.py
```