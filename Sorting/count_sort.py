# 계수 정렬(Count Sort)
# 특정한 조건이 부합할 때(데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때)만 사용할 수 있지만 매우 빠른 알고리즘
# 시간 복잡도 : O(N)

def count_sort(arr):
    count_arr = [0] * (len(arr) + 1)
    for n in arr:
        count_arr[n] += 1
    arr.clear()
    for i in range(len(count_arr)):
        for j in range(count_arr[i]):
            arr.append(i)


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print('정렬 전', array)
count_sort(array)
print('정렬 후', array)
