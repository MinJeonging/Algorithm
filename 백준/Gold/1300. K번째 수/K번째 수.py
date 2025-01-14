# 1300 K번째 수

"""

#### 문제 설명
- 배열 A[i][j]는 i × j로 이루어진 N × N 크기의 이차원 배열이다.
- 배열 A의 모든 원소를 일차원 배열 B로 만든 후 정렬했을 때, B[k]를 구하는 문제이다.

---

### 풀이 방법

#### 1. 이분 탐색의 적용
- K번째 수를 x라고 가정.
- x보다 작거나 같은 수가 배열 A에 K개보다 적게 존재한다면, x는 K번째 수가 될 가능성이 있다.
- 이를 기반으로 이분 탐색을 적용.

#### 2. 탐색 범위
- x의 가능한 범위는 [1, N^2].
- 중간 값 mid를 계산하고, mid 이하의 값 개수를 세어 K와 비교.

#### 3. 배열에서 mid 이하의 값 개수 구하기
- 배열 A에서 i번째 행에서 mid 이하인 값의 개수는 min(mid // i, N).
- 모든 행을 순회하며 합산하여 mid 이하의 값의 총 개수를 계산.

#### 4. 이분 탐색 조건
- mid 이하의 값 개수가 K보다 크거나 같으면 mid를 정답 후보로 저장하고 high = mid - 1.
- 그렇지 않으면 low = mid + 1.

---

### 구현 순서

1. low = 1, high = N^2.
2. 이분 탐색 반복:
   - mid = (low + high) // 2.
   - 배열 A에서 mid 이하의 값 개수 계산.
   - 개수와 K를 비교하여 low, high 갱신.
3. 탐색 종료 후 low 출력.

"""

N = int(input())
K = int(input())

low = 1
high = N * N
ans = -1

while low <= high:
    mid = (low + high) // 2

    count = 0
    for i in range(1, N + 1):
        # i, 2 * i, 3 * i, ..., N * i
        count += min(N, (mid - 1) // i)

    if count < K :
        ans = mid
        low = mid + 1
    else:
        high = mid - 1

print(ans)
