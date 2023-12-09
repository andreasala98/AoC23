import os, pathlib
import numpy as np

path = os.path.join(pathlib.Path(__file__).parent.parent, 'data', '09.in')

def part1and2():

    out, out2 = 0, 0

    with open(path, 'r') as f:
        lines = [[int(x) for x in line.split()] for line in f.read().split('\n')]

    for line in lines:

        history = [line]
        diffs = line

        while not all(d==0 for d in diffs):
            diffs = [diffs[i+1] - diffs[i] for i in range(len(diffs)-1)]
            history.append(diffs)

        out += sum([val[-1] for val in history])
        out2 += sum([val[0]*(-1)**(j) for j,val in enumerate(history)])

    print(out)
    print(out2)


if __name__ == '__main__':
    part1and2()