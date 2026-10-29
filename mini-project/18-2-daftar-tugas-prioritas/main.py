import heapq

pq = []
heapq.heappush(pq, (3, "Cuci piring"))
heapq.heappush(pq, (1, "Kerjakan PR"))
heapq.heappush(pq, (5, "Main game"))
heapq.heappush(pq, (2, "Belajar ujian"))
while pq:
    prioritas, nama = heapq.heappop(pq)
    print(str(prioritas) + ".", nama)
