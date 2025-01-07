# 14675 단절점과 단절선

N = int(input())
adj = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())

    adj[u - 1].append(v - 1) 
    adj[v - 1].append(u - 1) 

q = int(input())
for _ in range(q):
    t, k = map(int, input().split())

    good = False
    if t == 1 and len(adj[k - 1]) != 1:
        good = True
    
    if t == 2:
        good = True

    if good:
        print("yes")
    else:
        print("no")
