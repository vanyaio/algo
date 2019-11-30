import random
import itertools

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

def apply_perm(edges):
    v = len(edges)
    perm = ()
    while (perm == ()):
        for i in itertools.permutations([i for i in range(v)]):
            if (random.randint(1, v) == 1):
                perm = i
                break

    new_edges = [0 for i in range(v)]
    for i in range(v):
        new_edges[perm[i]] = edges[i]
    for i in range(v):
        for j in range(len(new_edges[i])):
            new_edges[i][j] = perm[new_edges[i][j]]
    return new_edges

def gen_by_ev(e_num, v_num):
    edges = [[] for i in range(v_num)]
    while e_num > 0:
        v1 = random.randint(0, v_num - 1)
        if (v1 == v_num - 1):
            continue
        v2 = random.randint(v1 + 1, v_num - 1)
        if (v2 in edges[v1]):
                continue
        else:
            edges[v1].append(v2)
            e_num -= 1
    return apply_perm(edges)

if __name__ == "__main__":
    edges = gen_by_ev(7, 5)
    print(edges)
    print(topsort(edges))
    
