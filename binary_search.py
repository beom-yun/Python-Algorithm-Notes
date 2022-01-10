# 재귀함수로 구현한 이진탐색
# array 안에 찾고자 하는 값(target)이 있으면 해당 인덱스 반환, 없으면 None 반환
def recursive_binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2        # 중간점, 소수점 이하는 버린다
    if array[mid] == target:        # 찾은 경우, 중간점 반환
        return mid
    elif array[mid] > target:       # 찾고자 하는 값이 중간점보다 왼쪽에 있는 경우
        return recursive_binary_search(array, target, start, mid - 1)
    else:                           # 찾고자 하는 값이 중간점보다 오른쪽에 있는 경우
        return recursive_binary_search(array, target, mid + 1, end)


# 반복문으로 구현한 이진탐색
# array 안에 찾고자 하는 값(target)이 있으면 해당 인덱스 반환, 없으면 None 반환
def repetitive_binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2        # 중간점, 소수점 이하는 버린다
        if array[mid] == target:
            return mid
        elif array[mid] > target:       # 찾고자 하는 값이 중간점보다 왼쪽에 있는 경우
            end = mid - 1
        else:                           # 찾고자 하는 값이 중간점보다 오른쪽에 있는 경우
            start = mid + 1
    return None


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    tar = 7                                                         # 찾으려는 값
    print(recursive_binary_search(arr, tar, 0, len(arr) - 1))       # 재귀
    print(repetitive_binary_search(arr, tar, 0, len(arr) - 1))      # 반복
