board = list(input())

count = 0
ans = ['X'] * len(board)

for idx, car in enumerate(board):
    if car == 'X':
        count += 1
        if (count % 4 != 0) and (count % 2 == 0):
            ans[idx-1], ans[idx] = 'B', 'B'
        elif count % 4 == 0:
            ans[idx-3], ans[idx-2], ans[idx-1], ans[idx] = 'A', 'A', 'A', 'A'
    elif car == '.':
        count = 0
        ans[idx] = '.'

ans = ''.join(ans)

if 'X' in ans:
    ans = -1

print(ans)