# 7795 먹을 것인가 먹힐 것인가

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 오름차순 정렬
    A.sort()
    B.sort()

    A_pointer = 0
    B_pointer = 0
    count = 0

    # A의 첫 원소, B의 첫 원소부터 탐색 시작
    # A_pointer > B_pointer : count += B_pointer + 1, B_pointer += 1
    # B_pointer >= A_pointer : A_pointer += 1
    # 종료조건: A_pointer > N - 1

    while A_pointer < N: # A는 N - 1까지 키울 수 있음.

        if B_pointer == M: # 엣지 케이스
            count += B_pointer
            A_pointer += 1
            
        else:
            if A[A_pointer] > B[B_pointer]: # 문제 요구 조건
                B_pointer += 1 

            else:
                count += B_pointer # B의 가능 원소 개수
                A_pointer += 1

    print(count)