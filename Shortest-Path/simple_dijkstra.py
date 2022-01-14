# 간단한 다익스트라 알고리즘
# 시간 복잡도 : O(V^2) / V: 노드의 개수


import sys

INF = int(1e9)      # 10억

n, m = map(int, sys.stdin.readline().split())           # n : 노드의 개수, m : 간선의 개수
start = int(sys.stdin.readline())                       # 시작 노드
graph = [[] for _ in range(n + 1)]                      # 각 노드에 연결되어 있는 노드들에 대한 정보
visited = [False] * (n + 1)                             # 방문여부
distance = [INF] * (n + 1)                              # 최단 거리 테이블

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])                             # a 노드에서 b 노드로 가는 비용이 c


# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호(인덱스) 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            index = i
            min_value = distance[i]
    return index


# 다익스트라 알고리즘
def dijkstra(start_node):
    # 시작 노드에 대해서 초기화
    distance[start_node] = 0
    visited[start_node] = True
    for i in graph[start_node]:
        distance[i[0]] = i[1]

    # 시작 노드를 제외한 노드에 대해서 반복
    for _ in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


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
