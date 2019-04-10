# -*- coding: utf-8 -*-

# Uva 11504 Dominos - componentes fortemente conexas

n = 0
part = []
count = 0
visit = []
adj = []
radj = []
node = []
N = 0


def Init(n):
    global visit, part, count, adj, radj, node
    visit = []
    part = []
    count = 0
    adj = []
    radj = []
    node = []
    for i in range(n):
        visit.append(True)
        part.append(0)
        adj.append([])
        radj.append([])


def DFS1(u):
    global visit, node, adj, N
    visit[u] = False
    for i in range(len(adj[u])):
        if visit[adj[u][i]]:
            DFS1(adj[u][i])
    node.append(u)


def DFS2(u, p):
    visit[u] = True
    part[u] = p
    for i in range(len(radj[u])):
        if not visit[radj[u][i]]:
            DFS2(radj[u][i], p)


def main():
    case = 0
    m = 0
    u = 0
    v = 0
    case = int(input())
    com = []
    var = ""
    result = []
    import sys
    sys.setrecursionlimit(1500)
    global visit, part, count, adj, radj, node, N
    while case:
        var = input()
        divide = var.split(' ')
        N = int(divide[0])
        m = int(divide[1])
        Init(N)
        com = []
        for i in range(N):
            com.append(True)
        for j in reversed(range(m)):
            line = input()
            pecas = line.split(' ')
            pos1 = int(pecas[0])
            pos2 = int(pecas[1])
            adj[pos1-1].append(pos2-1)
            radj[pos2-1].append(pos1-1)

        for i in range(N):
            if visit[i]:
                try:
                    DFS1(i)
                except:
                    pass
        npart = 0
        for i in reversed(range(len(node))):
            if not visit[node[i]]:
                try:
                    DFS2(node[i], npart)
                    npart += 1
                except:
                    pass
        for u in range(N):
            for i in range(len(adj[u])):
                v = adj[u][i]
                if (part[u] != part[v]):
                    com[part[v]] = False
        ans = 0
        i = 0
        for i in range(npart):
            if com[i]:
                ans += 1
        result.append(ans)
        case -= 1
    for i in result:
        print(i)
    return 0


if __name__ == "__main__":
    main()
