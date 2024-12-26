# 2217

N = int(input())
rope = [0] * N

for i in range(N):
    rope[i]= int(input())

rope.sort(reverse=True)

max_weight = 0

for idx in range(N):
    # (i + 1)개의 로프를 사용하는 경우에 들 수 있는 최대 무게를 구해줌.
    if max_weight < rope[idx] * (idx + 1):
        max_weight = rope[idx] * (idx + 1)

print(max_weight)
