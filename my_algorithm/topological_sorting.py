#tested with leetcode 210

def findOrder(n, edge):
    E = [[] for i in range(n)]
    print(E)
    for e in edge:
        E[e[1]].append(e[0])
    
    visit = [0] * n
    res = []

    def dfs(node, path):
        if visit[node] == 1:
            return False
        if (visit[node] == 2):
            return True
        visit[node] = 1
        for e in E[node]:
            if not dfs(e, path):
                return False
        visit[node] = 2
        path.append(node)
        return True

    for node in range(n):
        if visit[node] != 0:
            continue
        
        path = []
        st = dfs(node, path)
        if not st:
            return []
        print(path)
        res = res + path
    print(res)
    
    
# n= 4
# e =  [[1,0],[2,0],[3,1],[3,2]]

# sort_toplogical(n, e)