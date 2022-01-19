# Python-Algorithm-Notes
**코딩테스트 준비용 알고리즘 노트**

___

## 1. 그리디(Greedy)

`다익스트라` `플로이드 워셜` `거스름돈 문제`

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

## 3. 

___

## 4. 

___

## 5. 
