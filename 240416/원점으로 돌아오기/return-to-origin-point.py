N = int(input())
answer = 0
node = []
for i in range(N):
    x, y = map(int, input().split())
    node.append((x,y))


def dfs(x,y,visit):
    global answer
    if sum(visit) == N:
        if x == 0 or y == 0:
            answer += 1
        return
    
    for i in range(N):
        if visit[i] == 0 and (node[i][0] == x or node[i][1] == y):
            visit[i] = 1
            dfs(node[i][0],node[i][1],visit)
            visit[i] = 0


visit = [0 for _ in range(N)]
dfs(0,0,visit)
print(answer)