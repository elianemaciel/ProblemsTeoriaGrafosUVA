# -*- coding: utf-8 -*-

# uva 315 - Networking

mat =[]

n = 0
depth = []
lowpt = []
visited = []
cut = 0

def DFS(node, d, parent):
    back = 1000
    son = 0
    tmp = 0
    flag = 0
    global visited, cut, mat, n, depth, lowpt
    
    depth[node] = d
    for i in range(n):
        if mat[node][i]:
            if not visited[i]:
                visited[i] = 1
                tmp = DFS(i, d+1, node)
                if(tmp >= d):
                    flag = 1

                if(back > tmp):
                    back = tmp
                son += 1
            else:
                if(i != parent):
                    if back > depth[i]:
                        back = depth[i]

    lowpt[node] = back
    if(node == 0):
        if(son > 1):
            cut += 1
    else:
        cut += flag
    return lowpt[node]


def inicialize(N):
    global depth, lowpt, cut, visited, mat
    depth = []
    visited = []
    lowpt = []
    cut = 0
    mat =[]
    for i in range(N):
        lowpt.append(0)
        visited.append(0)
        depth.append(0)
        mat.append([])
        for j in range(N):
            mat[i].append(0)



def main():
    x = 0
    y = 0
    c = 0
    global visited, cut, mat, n, depth, lowpt
    num = 0
    result = []

    while True:
        try:
            n = int(input())
        except:
            break
        if not n:
            break
        inicialize(n)
        line = input()
        while line != '0':
            a = line.split(' ')
            k = int(a[0])-1
            for v in a[1:]:
                mat[k][int(v)-1] = 1
                mat[int(v)-1][k] = 1
            line = input()
        visited[0] = 1
        cut = 0
        DFS(0, 1, 0)
        result.append(cut)
    for i in result:
        print(i)
    return 0


if __name__ == "__main__":
    main()
