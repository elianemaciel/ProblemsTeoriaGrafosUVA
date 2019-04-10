# -*- coding: utf-8 -*-

# Ordenação Topológica uva 872 - Ordering
# Armazeno o grafo em uma matriz de adjacencias

used = []
G = []
ans = []
lin = []
N = 0
has = 0


def dfs(Idx):
    global N, has, used, G, lin, ans
    if(Idx == N):
        has = 1
        
        for i in range(N):
            if i == N-1:
                print(lin[ans[i]],  end="")
            else:
                print(lin[ans[i]],  end=" ")
        print("")
        return
    i = 0
    for i in range(N):
        if not used[i]:
            j = 0
            while j < Idx:
                if G[i][ans[j]]:
                    break
                j += 1
            if j == Idx:
                ans[Idx] = i
                used[i] = 1
                dfs(Idx+1)
                used[i] = 0


def inicialize(N):
    global used, ans, G
    used = []
    ans = []
    G = []
    for i in range(N):
        used.append(0)
        ans.append(0)
        G.append([])
        for j in range(N):
            G[i].append(0)


def main():
    global G, ans, lin, N, has, used
    line = True
    # import sys
    # sys.stdin = open('teste.txt')
    t = int(input())
    while t:
        white = input()
        line = input()
        lin = pega = []
        lin = line.split(' ')
        tam = len(lin)
        line2 = input()
        pega = line2.split(' ')
        N = tam
        has = 0
        inicialize(tam)
        for i in pega:
            dado = i.split('<')
            pos1 = lin.index(dado[0])
            pos2 = lin.index(dado[1])
            G[pos1][pos2] = 1
        dfs(0)
        t -= 1
        if not has:
            print("NO")
        if t:
            print("")
    return 0


if __name__ == "__main__":
    main()
