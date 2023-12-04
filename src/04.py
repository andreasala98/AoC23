import os, pathlib
import numpy as np

path = os.path.join(pathlib.Path(__file__).parent.parent, 'data', '04.in')


def part1():

    out = 0
    with open(path, 'r') as f:

        lines = f.read().split('\n')

        for line in lines:

            _, data = line.split(':')
            winning, my = data.strip().split('|')

            winning = winning.strip().replace('  ', ' ').split(' ')
            my = my.strip().replace('  ', ' ').split(' ')

            n_wins = sum(1 for n in my if n in winning)
            if n_wins > 0:
                out += 2**(n_wins-1)

        print(out)


def part2():

    out = 0
    with open(path, 'r') as f:

        lines = f.read().split('\n')
        multiplier = [1]*len(lines)

        for i, line in enumerate(lines):

            _, data = line.split(':')
            winning, my = data.strip().split('|')

            winning = winning.strip().replace('  ', ' ').split(' ')
            my = my.strip().replace('  ', ' ').split(' ')

            n_wins = sum(1 for n in my if n in winning)

            for _ in range(multiplier[i]):
                for j in range(n_wins):
                    multiplier[i+j+1] += 1

        out = sum(multiplier)
        print(out)

if __name__ == '__main__':

    part1()
    part2()