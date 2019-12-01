import random
import statistics
import itertools
import time
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from p1 import *

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

def draw(es, vs, ts, z_str, title_str):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(np.array(es), np.array(vs), np.array(ts))
    ax.set_xlabel("E")
    ax.set_ylabel("V")
    ax.set_zlabel(z_str)
    ax.set_title(title_str)
    plt.show()

def main():
    sum = 1000
    steps = 11 
    delta = 100
    ratio = 3
    es = []
    vs = []
    ts = []
    sumarr = []
    rel = []
    for i in range(steps):
        sumarr.append(sum)
        e, v = get_ev_by_sum(sum, ratio)
        edges = gen_by_ev(e, v)
        e2, v2 = get_ev_by_sum(2 * sum, ratio)
        edges2 = gen_by_ev(e2, v2)
        
        av = []
        av2 = []
        rel_av = []
        for j in range(10):
            start = time.time()
            topsort(edges)
            end = time.time()
            t = end - start
            av.append(t)

            start = time.time()
            topsort(edges2)
            end = time.time()
            t2 = end - start
            av2.append(t2)
            rel_av.append(t2 / t)
            
        av = statistics.mean(av)
        av2 = statistics.mean(av2)
        rel_av = statistics.mean(rel_av)

        es.append(e)
        vs.append(v)
        ts.append(av)
        rel.append(rel_av)

        sum += delta

    draw(es, vs, ts, "time(sec)", "Time from Edges and Vertices")
    draw(es, vs, rel, "double-ratio", "double-ratio from Edges and Vertices")
    print("Sum, Time")
    for i in range(len(sumarr)):
        print(str(sumarr[i]) + " " + str(ts[i]))
    print("Sum, double-ratio")
    for i in range(len(sumarr)):
        print(str(sumarr[i]) + " " + str(rel[i]))



if __name__ == "__main__":
    #  edges = gen_by_ev(7, 5)
    #  print(edges)
    #  print(topsort(edges))
    main()
    
