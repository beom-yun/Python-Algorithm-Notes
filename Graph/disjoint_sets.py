# 서로소 집합(Disjoint Sets)
# 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조, union과 find 2개의 연산으로 조작 가능하다
# union 연산 : 2개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
# find 연산 : 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산

# 특정 원소가 속한 집합을 찾기, 해당 집합의 루트 노드 반환(find 연산)
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기(union 연산)
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


if __name__ == '__main__':
    # 노드의 개수(v)와 간선(union 연산)의 개수(e) 입력받기
    v, e = map(int, input().split())
    parent_list = [i for i in range(v + 1)]     # 각 노드의 부모를 자기 자신으로 초기화

    # union 연산 수행
    for _ in range(e):
        i, j = map(int, input().split())
        union_parent(parent_list, i, j)

    # union 연산 이후, 모든 노드들에 대해 find 함수 수행 : 부모 테이블 갱신하기 위함
    for i in range(1, v + 1):
        find_parent(parent_list, i)

    print('parent_list:', parent_list[1:])

# 예시 입력
# 6 4   # v, e
# 1 4
# 2 3
# 2 4
# 5 6
# 결과 : [1, 1, 1, 1, 5, 5]
# {1, 2, 3, 4}는 부모가 전부 1로써 하나의 집합, {5, 6}은 부모가 5로써 하나의 집합 / {1, 2, 3, 4}과 {5, 6}은 서로소 집합
