import os, pathlib
from itertools import product
from collections import Counter
from tqdm import trange

path = os.path.join(pathlib.Path(__file__).parent.parent, 'data', '12.in')

def is_valid(code, num):

    canc_seq = [c.replace('.','') for c in code.split('.')]
    lens = [len(c) for c in canc_seq if len(c)>0]

    return lens == num


def part1():

    out = 0
    with open(path, 'r') as f:
        lines = f.read().split('\n')

    codes = [line.split()[0] for line in lines]
    nums = [[int(n) for n in line.split()[1].split(',')] for line in lines]

    for i in trange(len(codes)):

        n_quest = Counter(codes[i])['?']

        for trial in list(product([0,1], repeat=n_quest)):
            new_code = ''
            k = 0
            for j in range(len(codes[i])):
                if codes[i][j]=='?':
                    new_code += '#' if trial[k]==1 else '.'
                    k += 1
                else:
                    new_code += codes[i][j]
            
            if is_valid(new_code, nums[i]):
                out += 1

    print(out)


if __name__ == '__main__':

    part1()