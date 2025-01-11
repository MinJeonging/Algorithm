# 6550 부분 문자열

# 주의. 테스트 횟수가 주어지지 않음.
while True:
    try:
        S, T = input().split()

        s_pointer = 0
        t_pointer = 0

        while True:
            if s_pointer == len(S): # 성공 종료
                print("Yes")
                break
            if t_pointer == len(T): # 실패 종료
                print("No")
                break 

            if S[s_pointer] == T[t_pointer]:
                s_pointer += 1
                t_pointer += 1

            else:
                t_pointer += 1


    except: # 에러가 뜨면 종료
        break