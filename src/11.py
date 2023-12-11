import os, pathlib
import numpy as np
from itertools import combinations
from tqdm import trange

path = os.path.join(pathlib.Path(__file__).parent.parent, 'data', '11.in')

N_EXP = 999999

def manhattan(g1, g2):

    return np.sum(np.abs(g1 - g2))

def part1():
    out = 0

    with open(path, 'r') as f:
        lines = f.read().split('\n')
        
    N, M = len(lines), len(lines[0])
    G = np.zeros((N, M), dtype=int)
    print(N, M)

    for i in range(N):
        for j in range(M):
            if lines[i][j]=='#':
                G[i][j]=1

    G_old = G

    n_ins = 0
    for i in trange(N):
        if np.sum(G_old[i])==0:
            G = np.insert(G, i+n_ins, np.zeros((M)), 0)
            n_ins += 1

    n_ins = 0
    N = len(G)

    for j in trange(M):
        if np.sum(G_old[:, j])==0:
            G = np.insert(G, j+n_ins, np.zeros((N)), 1)
            n_ins += 1

    galaxies = np.argwhere(G==1)


    for g1, g2 in combinations(galaxies, 2):

        out += manhattan(g1, g2)

    print(out)


def part2():

    out = 0

    with open(path, 'r') as f:
        lines = f.read().split('\n')

    N, M = len(lines), len(lines[0])
    G = np.zeros((N, M), dtype=int)

    for i in range(N):
        for j in range(M):
            if lines[i][j]=='#':
                G[i][j]=1

    G_old = G

    n_ins = 0
    for i in trange(N):
        if np.sum(G_old[i])==0:
                G = np.insert(G, i+n_ins, np.zeros((N_EXP, M)), 0)
                n_ins += N_EXP

    N = len(G)

    n_ins = 0

    G_new = G_old.T

    for i in trange(M):
        if np.sum(G_old[:, i])==0:
            G_new = np.insert(G_new, i+n_ins, np.zeros((N_EXP, len(G_old)), dtype=int), 0)
            n_ins += N_EXP

    G_new = G_new.T
    M = len(G[0])

    # print(G)
    # print(G_new)

    galaxies = np.argwhere(G==1)

    for g1, g2 in combinations(galaxies, 2):
        # print(g1, g2, abs(g1[1] - g2[1]))
        out += abs(g1[0] - g2[0])

    galaxies2 = np.argwhere(G_new==1)

    for g1, g2 in combinations(galaxies2, 2):
        out += abs(g1[1] - g2[1])
        

    print(out)



if __name__ == '__main__':

    part1()
    part2()