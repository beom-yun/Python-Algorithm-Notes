# BFS(너비 우선 탐색, Breadth First Search)
# 그래프에서 가까운 노드부터 탐색하는 알고리즘
# 큐 자료구조 사용, deque 라이브러리로 구현
# 시간 복잡도 : O(N)

from collections import deque


def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True                   # 시작 노드 방문처리

    while q:                                # 큐가 빌 때까지 반복
        v = q.popleft()
        print(v, end=' ')
        for vertex in graph[v]:             # 해당 원소와 연결된, 아직 방문하지 않은 노드들을 큐에 삽입
            if not visited[vertex]:
                q.append(vertex)
                visited[vertex] = True


# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph_list = [
    [],
    [2, 3, 8],      # 1
    [1, 7],         # 2
    [1, 4, 5],      # 3
    [3, 5],         # 4
    [3, 4],         # 5
    [7],            # 6
    [2, 6, 8],      # 7
    [1, 7]          # 8
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited_list = [False] * 9

# 1번 노드부터 탐색 시작
bfs(graph_list, 1, visited_list)

# 결과 : 1 2 3 8 7 4 5 6
