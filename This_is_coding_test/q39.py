# Q39 화성 탐사

import heapq

t = int(input())
INF = int(1e9)

for _ in range(t):
    n = int(input())
    distance = [INF] * (n * n)
    # 2차원으로 입력되는 그래프를 다익스트라 적용시키기 위해 1차원으로 변경
    graph = [[] for _ in range(n * n)]
    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(n):
            # print('(' + str(i) + ', ' + str(j) + ') 에 대해서' + str(i * n + j))
            for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                if 0 <= i + di < n and 0 <= j + dj < n:
                    # print('(' + str(i + di) + ', ' + str(j + dj) + ') 검사')
                    graph[i * n + j].append(((i + di) * n + (j + dj), data[i + di][j + dj]))

    # print(graph)

    # 시작노드는 (0, 0), 다익스트라 실행
    q = []
    start_node = 0
    distance[0] = data[0][0]
    heapq.heappush(q, (data[0][0], 0))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    print(distance)
