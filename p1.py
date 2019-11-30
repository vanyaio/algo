import random
import itertools
import time
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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
        ls = [i for i in range(v)]
        it = itertools.permutations(ls)
        for i in it:
            if (random.randint(1, 100) == 1):
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

def get_ev_by_sum(sum, ratio):
    #  while True:
        #  e = random.randint(0, sum - 1)
        #  v = sum - e
        #  if (e > (v - 1) * v / 2):
            #  continue
        #  else:
            #  return (e, v)
    # To proof linear keep v/e the same during experiment
    v = sum // ratio
    e = sum - v
    if (e > (v - 1) * v / 2):
        print("ratio is incorrect!!!")
    return (e, v)

def draw(es, vs, ts):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(np.array(es), np.array(vs), np.array(ts))
    ax.set_xlabel("E")
    ax.set_ylabel("V")
    ax.set_zlabel("time(sec)")
    ax.set_title("Time from Edges and Vertices")
    plt.show()

def main():
    sum = 10000
    steps = 15
    delta = 1000
    ratio = 5 
    es = []
    vs = []
    ts = []
    for i in range(steps):
        e, v = get_ev_by_sum(sum, ratio)
        edges = gen_by_ev(e, v)
        
        start = time.time()
        topsort(edges)
        end = time.time()

        es.append(e)
        vs.append(v)
        ts.append(end - start)

        sum += delta

    draw(es, vs, ts)


if __name__ == "__main__":
    #  edges = gen_by_ev(7, 5)
    #  print(edges)
    #  print(topsort(edges))
    main()
    
