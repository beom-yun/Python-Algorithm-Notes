# Q40 숨바꼭질

import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    # 양방향 길이기 때문
    graph[a].append((b, 1))
    graph[b].append((a, 1))

distance = [int(1e9)] * (n + 1)
q = []
distance[1] = 0
heapq.heappush(q, (0, 1))

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue

    for i in graph[now]:
        cost = dist + i[1]
        if distance[i[0]] > cost:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

max_num = max(distance[1:])
print(distance[1:].index(max_num) + 1, max_num, distance[1:].count(max_num))
