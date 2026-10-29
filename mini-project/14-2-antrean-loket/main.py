from collections import deque

q = deque()
for n in ["Ani", "Budi", "Cici", "Dodi"]:
    q.append(n)
while q:
    orang = q.popleft()
    print("Melayani", orang + ", sisa", list(q))
