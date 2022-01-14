# 개선된 다익스트라 알고리즘
# 시간 복잡도 : O(ElogV) / E: 간선의 개수, V: 노드의 개수

import heapq
import sys

INF = int(1e9)      # 10억

n, m = map(int, sys.stdin.readline().split())           # n : 노드의 개수, m : 간선의 개수
start = int(sys.stdin.readline())                       # 시작 노드
graph = [[] for _ in range(n + 1)]                      # 각 노드에 연결되어 있는 노드들에 대한 정보
distance = [INF] * (n + 1)                              # 최단 거리 테이블

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])                             # a 노드에서 b 노드로 가는 비용이 c


# 개선된 다익스트라 알고리즘
def dijkstra(start_node):
    q = []
    heapq.heappush(q, (0, start_node))                  # 시작 노드(start_node)로 가기 위한 최단 경로는 0, 큐에 삽입
    distance[start_node] = 0

    while q:                                            # 큐가 비어있지 않다면
        dist, now = heapq.heappop(q)                    # 가장 최단거리가 짧은 노드 정보 꺼내기
        if distance[now] < dist:                        # 현재 노드가 이미 처리된 적이 있다면 무시
            continue
        for i in graph[now]:                            # 현재 노드와 연결된 다른 이접한 노드들을 확인
            cost = dist + i[1]
            if cost < distance[i[0]]:                   # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# 알고리즘 수행
dijkstra(start)

# 출력
for k in range(1, n + 1):
    if distance[k] == INF:
        print('INFINITY', end=' ')
    else:
        print(distance[k], end=' ')


# 예시 입력(답: 0 2 3 1 2 4)
# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2
