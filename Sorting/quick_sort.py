# 퀵 정렬(Quick Sort)
# 기준 데이터를 설정하고(pivot) 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾼다
# 시간 복잡도 : O(NlogN)
# 최악의 경우(데이터가 이미 정렬되어 있는 경우) 퀵 정렬은 매우 느리게 동작하며 시간복잡도는 O(N^2)이다

def quick_sort(arr):
    if len(arr) <= 1:           # 리스트가 하나 이하의 원소만을 가진다면 종료
        return arr

    pivot = arr[0]              # 피벗은 첫 번째 원소
    tail = arr[1:]              # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]     # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]     # 분할된 오른쪽 부분

    # print('pivot, tail:', pivot, tail)
    # print('left side:', left_side)
    # print('right side:', right_side)
    # print()

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print('정렬 전', array)
quick_sort(array)
print('정렬 후', array)
