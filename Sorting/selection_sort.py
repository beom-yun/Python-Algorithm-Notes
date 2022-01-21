# 선택 정렬(Selection Sort)
# 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸고 ... (반복)
# 시간 복잡도 : O(N^2)

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print('정렬 전', array)
selection_sort(array)
print('정렬 후', array)
