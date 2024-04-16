N = int(input())
answer = 0
node = []
for i in range(N):
    x, y = map(int, input().split())
    node.append((x, y))


def find_d(tp, u, v):
    if tp == 'x':
        if u > v:
            return 2
        else:
            return 4
    else:
        if u > v:
            return 1
        else:
            return 3


def dfs(x, y, visit, direction):
    global answer
    if sum(visit) == N:
        d = direction
        if x == 0:
            d = find_d('x', 0, y)
        elif y == 0:
            d = find_d('y', 0, x)

        if d != direction:
            answer += 1

        return

    for i in range(N):
        if visit[i] == 0:
            if node[i][0] == x:
                d = find_d('x', node[i][1], y)
                if d != direction:
                    visit[i] = 1
                    dfs(node[i][0], node[i][1], visit, d)
                    visit[i] = 0

            elif node[i][1] == y:
                d = find_d('y', node[i][0], x)
                if d != direction:
                    visit[i] = 1
                    dfs(node[i][0], node[i][1], visit, d)
                    visit[i] = 0


visit = [0 for _ in range(N)]
dfs(0, 0, visit, 0)
print(answer)