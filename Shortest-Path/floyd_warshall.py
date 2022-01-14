# 플로이드 워셜 알고리즘
# 모든 노드에서 다른 모든 노드까지의 최단 경로를 모두 구함
# 시간복잡도 : O(N^3)

INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]


# 그래프 출력
def print_graph():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(graph[i][j], end=' ')
        print()


# 자기 자신 -> 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c                             # a에서 b로 가는 비용은 c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
# 'a에서 b로 가는 비용' = min('a에서 b로 가는 비용', 'a에서 k로 가는 비용' + 'k에서 b로 가는 비용')
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

print_graph()
