def dfs(v, used, ans, edges):
    used[v] = True
    for i in edges[v]:
        if (not used[i]):
            dfs(i, used, ans, edges);
    ans.append(v)

def topsort(edges):
    v = len(edges)
    used = [False for i in range(v)]
    ans = []
    for i in range(v):
        if (not used[i]):
            dfs(i, used, ans, edges)
    ans.reverse()
    return ans
