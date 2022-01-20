# DFS(깊이 우선 탐색, Depth First Search)
# 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
# 스택 자료구조 사용, 재귀함수로 구현
# 시간 복잡도 : O(N)

def dfs(graph, v, visited):
    visited[v] = True                   # 현재 노드를 방문 처리
    print(v, end=' ')
    for i in graph[v]:                  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        if not visited[i]:
            dfs(graph, i, visited)


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
dfs(graph_list, 1, visited_list)

# 결과 : 1 2 7 6 8 3 4 5
