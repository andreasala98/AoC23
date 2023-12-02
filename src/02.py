import os, pathlib
import numpy as np

path = os.path.join(pathlib.Path(__file__).parent.parent, 'data', '02.in')

max_blue, max_red, max_green = 14, 12, 13

def get_numbers(subset):

    words = subset.replace(',', ' ').split()
    blue = red = green = 0

    for i, word in enumerate(words):
        if word=='blue':
            blue = int(words[i-1])
        elif word=='red':
            red = int(words[i-1])
        elif word=='green':
            green = int(words[i-1])
    
    return [blue, red, green]

def is_allowed(score):
    return score[0]<=max_blue and score[1]<=max_red and score[2]<=max_green


def part1():

    out = 0

    with open(path, 'r') as f:

        lines = f.read().split('\n')

    for line in lines:
        game, data = line.split(':')
        n = int(game.split(' ')[-1])

        scores = [get_numbers(comb) for comb in data.split(';')]
        allowed = [is_allowed(sc) for sc in scores]

        if False not in allowed:
            out += n

    print(out)


def part2():

    out = 0

    with open(path, 'r') as f:

        lines = f.read().split('\n')

    for line in lines:
        game, data = line.split(':')
        n = int(game.split(' ')[-1])

        scores = np.asarray([get_numbers(comb) for comb in data.split(';')])
        power = max(scores[:,0]) * max(scores[:,1]) * max(scores[:,2])

        out += power

    print(out)


if __name__ == '__main__':
    part1()
    part2()