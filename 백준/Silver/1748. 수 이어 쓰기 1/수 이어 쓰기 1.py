N = int(input())

cur = 9 
ans = 9
i = 1

if N // cur == 0:
    ans = N

while N // cur != 0:
    i += 1
    cur = int('9'* i)

    ans += (min(N, cur) - int('9'* (i - 1))) * len(str(cur))
    ans = int(ans)

print(ans)