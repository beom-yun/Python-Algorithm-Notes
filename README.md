# Python-Algorithm-Notes
**코딩테스트 준비용 알고리즘 노트**

___

## 1. 그리디(Greedy)

`다익스트라` `거스름돈 문제`

### 현재 상황에서 지금 당장 좋은 것만 고르는 방법.

* 그리디 알고리즘을 이용하면 **매 순간 가장 좋아 보이는 것을 선택**하며, 현재의 선택이 나중에 미칠 영향에 대해서는 고려하지 않는다.

* 코딩 테스트에서의 그리디 알고리즘의 문제 유형은 대부분 사전에 외우고 있지 않아도 풀 수 있을 가능성이 높은 문제 유형이다.(다익스트라 같은 특정 알고리즘 제외)

* 그리디 알고리즘은 기준에 따라 좋은 것을 선택하는 알고리즘이므로 문제에서 ‘가장 큰 순서대로’, ‘가장 작은 순서대로’와 같은 기준을 알게 모르게 제시해주며 대체로 정렬 알고리즘과 짝을 이뤄 출제된다.

### 그리디 알고리즘의 정당성

* 그리디 알고리즘을 이용했을 때 ‘최적의 해’를 찾을 수 없을 가능성이 다분하다. 문제 풀이를 위한 최소한의 아이디어를 떠올리고 이것이 **정당한지 검토**할 수 있어야 한다.

___

## 2. 구현(Implementation)

### 머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정

* 흔히 문제 해결 분야에서 구현 유형의 문제는 ‘풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제’를 의미한다. 피지컬을 요하는 문제.

  * `완전 탐색` 모든 경우의 수를 주저 없이 다 계산하는 해결 방법

  * `시뮬레이션` 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행

### 구현 시 고려해야 할 메모리 제약 사항

* 대체로 코딩 테스트에서는 128 ~ 512MB로 메모리를 제한한다.

* 파이썬에서는 정수 데이터를 사용할 때 int와 같은 별도의 자료형을 명시해줄 필요가 없지만, 시스템 내부적으로는 다음 표에서 보여주는 것과 유사한 크기만큼 메모리를 차지한다.

    데이터의 개수(리스트 길이) | 메모리 사용량
    :---:|:---:
    1,000|약 4KB
    1,000,000|약 4MB
    10,000,000|약 40MB

### 채점 환경

* 대부분의 채점 시스템의 시간 제한은 1초이다.

* 일반적인 기업 코딩 테스트 환경에서는 파이썬 코드가 1초에 2,000만 번의 연산을 수행한다고 가정하면 크게 무리가 없다.

* 시간 제한이 1초이고, 데이터의 개수가 100만 개인 문제가 있다면 일반적으로 시간 복잡도 O(NlogN) 이내의 알고리즘을 이용하여 문제를 풀어야 한다. (N = 1,000,000일 때 NlogN = 약 20,000,000)

___

## 3. 탐색(Search)

`BFS` `DFS` `순차 탐색` `이진 탐색`

### 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정

* 프로그래밍에서는 그래프, 트리 등의 자료구조 안에서 탐색을 하는 문제를 자주 다룸

### DFS / BFS

* `DFS(Depth First Search)`

  * **깊이 우선 탐색**이라고도 부르며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘

  * 스택 자료구조 사용
  
    ```
    1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
    2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다.
       방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
    3. 2.번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.
    ```

* `BFS(Breadth First Search)`

  * **너비 우선 탐색**이라고도 부르며, 그래프에서 가까운 노드부터 탐색하는 알고리즘

  * 큐 자료구조 사용

  * 일반적인 경우 실제 수행 시간은 DFS보다 BFS가 좋은 편

    ```
    1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
    2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
    3. 2.번의 과정을 더 이상 수행할 수 없을 때까지 반복한다(큐가 빌 때까지).
    ```

### 순차 탐색 / 이진 탐색

* `순차 탐색(Sequential Search)`

  * 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법

  * 시간 복잡도 : O(N)

* `이진 탐색(Binary Search)` 반으로 쪼개면서 탐색하기

  * 탐색하고자 하는 범위(시작점(Start) ~ 끝점(End))안에서 찾으려는 데이터와 중간점(Middle) 위치에 있는 데이터를 반복적으로 비교

  * 시간 복잡도 : O(logN)

  * 이진 탐색은 코딩 테스트에서 단골로 나오는 문제이니 외우자

___

## 4. 정렬(Sorting)

`선택 정렬` `삽입 정렬` `퀵 정렬` `계수 정렬`

### 데이터를 특정한 기준에 따라서 순서대로 나열하는 것

* 프로그램에서 데이터를 가공할 때 오름차순이나 내림차순 등 어떤 식으로든 정렬해서 사용하는 경우가 많기에 정렬 알고리즘을 프로그램을 작성할 때 가장 많이 사용되는 알고리즘 중 하나다.

* 이진 탐색의 전처리 과정

### 선택 정렬(Selection Sort)

* 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸고 ... (반복)

* 시간 복잡도 : O(N^2)

### 삽입 정렬(Insertion Sort)

* 데이터를 하나씩 확인하며, 각 데이터를 적절한 위치에 삽입

* 데이터가 거의 정렬되어 있을 때 효율적(최선의 경우 O(N)이며 퀵 정렬 알고리즘보다 더 강력하다)

* 시간 복잡도 : O(N^2)

### 퀵 정렬(Quick Sort)

* 기준 데이터를 설정하고(pivot) 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾼다

* 시간 복잡도 : O(NlogN)

* 최악의 경우(데이터가 이미 정렬되어 있는 경우) 퀵 정렬은 매우 느리게 동작하며 시간복잡도는 O(N^2)이다

### 계수 정렬(Count Sort)

* 특정한 조건이 부합할 때(데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때)만 사용할 수 있지만 매우 빠른 알고리즘

* 시간 복잡도 : O(N)

### 파이썬의 정렬 라이브러리

* 병합 정렬과 삽입 정렬의 아이디어를 더한 하이브리드 방식의 정렬 알고리즘. 항상 최악의 경우에도 시간 복잡도 O(NlogN)을 보장한다.

  ```python
  array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
  result = sorted(array)    # 결과를 반환
  arrary.sort()             # 결과 반환 X
  ```

___

## 5. 다이나믹 프로그래밍(Dynamic Programming)

`피보나치수열` `LIS` `플로이드 워셜`

### 메모리 공간을 약간 더 사용하며 연산 속도를 비약적으로 증가시키는 방법

* 큰 문제를 작게 나누고, 같은 문제라면 한 번씩만 풀어 문제를 효율적으로 해결하는 알고리즘 기법. 주로 점화식으로 나타내어 해결한다. 동적 계획법이라고도 부른다.

  ```
  * 다이나믹 프로그래밍을 사용하기 위한 조건
      1. 큰 문제를 작은 문제로 나눌 수 있다.
      2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.
  ```

* 프로그래밍에서 다이나믹은 ‘프로그램이 실행되는 도중에’라는 의미이다. 자료구조에서 동적 할당(Dynamic Allocation)은 프로그램 실행 중에 프로그램 실행에 필요한 메모리를 할당하는 기법이다. 하지만 다이나믹 프로그래밍에서의 ‘다이나믹’과 다른 의미이다.

* 탑다운 / 보텀업

  * `탑다운(Top-Down)` `메모이제이션` 재귀 함수를 이용하여 큰 문제를 해결하기 위해 작은 문제를 호출

  * `보텀업(Bottom-Up)` 단순히 반복문을 이용하여 작은 문제부터 차근차근 답을 도출. 결과 저장용 리스트는 **DP 테이블**이라 부른다.

___

## 6. 그래프(Graph) 관련 알고리즘

`다익스트라` `플로이드 워셜`

### 그래프를 표현하는 2가지 방법

* `인접 행렬(Adjacency Matrix)` 2차원 배열로 그래프의 연결 관계를 표현하는 방식

* `인접 리스트(Adjacency List)` 리스트로 그래프의 연결 관계를 표현하는 방식

  인접 행렬 | vs | 인접 리스트
  :---:|:---:|:---:
  불필요하게 낭비|메모리|효율적
  빠르다|정보를 얻는 속도|느리다

### 최단 경로(Shortest Path) 알고리즘

* 다익스트라(Dijkstra) 최단 경로 알고리즘

  * 한 지점에서 다른 특정 지점까지의 최단 경로를 구하는 알고리즘. 그리디.

  ```
  1. 출발 노드를 설정한다.
  2. 최단 거리 테이블을 초기화한다.
  3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.
  4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
  5. 3.과 4.를 반복한다.
  ```

* 플로이드 워셜(Floyd-Warshall) 알고리즘

  * 모든 지점에서 다른 모든 지점까지의 최단 경로를 구하는 알고리즘. 다이나믹 프로그래밍.
  
  * 특정 노드(k)를 거쳐가는 경우를 고려. Dab = min(Dab, Dak + Dkb)
  
  * 시간 복잡도 : O(N^3)

___

## 7. 자료구조(Data Structure) 기초

### 데이터를 표현하고 관리하고 처리하기 위한 구조

### 스택(Stack)

* 선입후출(FILO) 구조 또는 후입선출(LIFO) 구조

* 파이썬에서 스택은 기본 라이브러리 사용

### 큐(Queue)

* 선입선출(FIFO) 구조

* 파이썬에서 큐를 구현할 때는 collections 모듈에서 제공하는 deque 자료구조 활용

  ```python
  from collections import deque
  
  q = deque()
  q.append(3)
  q.popleft()
  q.reverse()
  ```

### 우선순위 큐(Priority Queue)

* 가장 우선순위가 높은 데이터를 가장 먼저 삭제

* 대부분 프로그래밍 언어에서(파이썬 포함) 우선순위 큐 라이브러리에 데이터의 묶음을 넣으면, 첫 번째 원소를 기준으로 우선순위를 설정한다.

* 파이썬 라이브러리에서는 기본적으로 **최소 힙(Min Heap)** 구조(값이 낮은 데이터가 먼저 삭제)

  ```python
  import heapq
  ```

### 재귀 함수(Recursive Function)

* 자기 자신을 다시 호출하는 함수

* 재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수가 언제 끝날지, 종료 조건을 꼭 명시해야 한다.

* 내부적으로 스택 자료구조와 동일하기 때문에, 스택 자료구조를 활용해야 하는 상당수 알고리즘은 재귀 함수를 이용해서 간편하게 구현될 수 있다.(ex DFS)

___

## 8. 중요한 파이썬 표준 라이브러리 & 알면 좋은 함수

### 내장함수

### itertools

### heapq

### bisect

### collections

### math

  ```python
  string = 'abcde'
  s1 = string.rjust(10, 'A')
  s2 = string.ljust(7, 'Z')
  print(s1)
  print(s2)
  # AAAAAabcde
  # abcdeZZ
  ```
