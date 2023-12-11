import os, pathlib
import numpy as np
from itertools import combinations
from tqdm import trange

path = os.path.join(pathlib.Path(__file__).parent.parent, 'data', '11.in')

N_EXP = 999999

def manhattan(g1, g2):

    return np.sum(np.abs(g1 - g2))

def part2():

    out = 0

    with open(path, 'r') as f:
        lines = f.read().split('\n')
        
    N, M = len(lines), len(lines[0])
    G = np.zeros((N, M), dtype=bool)

    for i in range(N):
        for j in range(M):
            if lines[i][j]=='#':
                G[i][j]=1

    G_old = G
    print(G.shape)
    n_ins = 0
    for i in trange(N):
        if np.sum(G_old[i])==0:
                G = np.insert(G, i+n_ins, np.zeros((N_EXP, M)), 0)
                n_ins += N_EXP

    N = len(G)
    print(G.shape)
    n_ins = 0

    G = G.T

    for i in trange(M):
        if np.sum(G_old[:, i])==0:
            G = np.insert(G, i+n_ins, np.zeros((N_EXP, N)), 0)
            n_ins += N_EXP

    G = G.T
    M = len(G[0])
    print(G.shape)
    galaxies = np.argwhere(G==1)

    for g1, g2 in combinations(galaxies, 2):
        out += manhattan(g1, g2)


    print(out)





if __name__ == '__main__':

    part2()