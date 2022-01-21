# 삽입 정렬(Insertion Sort)
# 데이터를 하나씩 확인하며, 각 데이터를 적절한 위치에 삽입
# 데이터가 거의 정렬되어 있을 때 효율적(최선의 경우 O(N)이며 퀵 정렬 알고리즘보다 더 강력하다)
# 시간 복잡도 : O(N^2)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):       # 인덱스 i부터 1까지 감소하며 반복
            if arr[j] < arr[j - 1]:     # 왼쪽 데이터가 크다면, 한 칸씩 왼쪽으로 이동
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print('정렬 전', array)
insertion_sort(array)
print('정렬 후', array)
