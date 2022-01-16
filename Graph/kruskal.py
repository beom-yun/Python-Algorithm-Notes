# 크루스칼 알고리즘(Kruskal Algorithm)
# 신장 트리 중에서 최소 비용으로 만들 수 있는 신장 트리를 찾는 알고리즘
#  - 신장 트리(Spanning Tree) : 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프

# 특정 원소가 속한 집합을 찾기(find 연산)
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 찾기(union 연산)
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


if __name__ == '__main__':
    v, e = map(int, input().split())            # 노드의 개수(v), 간선의 개수(e) 입력받기
    parent_list = [n for n in range(v + 1)]     # 부모 테이블에서, 부모를 자기 자신으로 초기화

    edges = []                                  # 모든 간선을 담을 리스트
    result = 0                                  # 최종 비용을 담을 변수

    # 모든 간선에 대한 정보 입력받기
    for _ in range(e):
        a, b, cost = map(int, input().split())  # a에서 b로 가는 비용이 cost
        edges.append((cost, a, b))              # 비용(cost)순으로 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정

    edges.sort()                                # 튜플의 첫 번째 요소(비용)로 정렬

    # 간선을 하나씩 확인해가며
    for edge in edges:
        cost, a, b = edge
        # find 연산 수행 후, 사이클이 발생하지 않는 경우에만 집합에 포함(union 연산)
        if find_parent(parent_list, a) != find_parent(parent_list, b):
            union_parent(parent_list, a, b)
            result += cost

    print(result)

# 예시 입력
# 7 9
# 1 2 29
# 1 5 75
# 2 3 35
# 2 6 34
# 3 4 7
# 4 6 23
# 4 7 13
# 5 6 53
# 6 7 25
# 결과 : 159
