import os, pathlib
from collections import Counter
import numpy as np

path = os.path.join(pathlib.Path(__file__).parent.parent, 'data', '07.in')

conv = {'A': 1, 'K': 12/13, 'Q': 11/13, 'J': 10/13, 'T': 9/13}
conv.update({str(i): (i-1)/13 for i in range(2, 10)})

conv2 = {'A': 1, 'K': 12/13, 'Q': 11/13, 'T': 10/13, 'J': 1/13}
conv2.update({str(i): i/13 for i in range(2,10)})


def get_score(play, conv_dict):

    return get_base_score(play) + get_added_score(play, conv_dict)


def get_base_score(play):
    cnt = Counter(list(play))
    keys = cnt.values()

    base_score = 0

    if max(keys)==5:      #manita
        base_score = 7e10

    elif max(keys)==4:    #poker
        base_score = 6e10

    elif max(keys)==3 and 2 in keys:  #full house
        base_score = 5e10

    elif max(keys)==3:    #three
        base_score = 4e10

    elif max(keys)==2 and sorted(keys)[-2]==2: #two pairs
        base_score = 3e10
    
    elif max(keys)==2:     #pair
        base_score = 2e10
    
    else:
        base_score = 1e10

    return base_score


def get_added_score(play, conv_dict):

    lplay = list(play)
    add_score = sum([conv_dict[card] * 10 **(8-2*i) for i, card in enumerate(lplay)])

    return add_score



def get_score_2(play):

    lplay = list(play)

    if 'J' in play:

        tries = []

        for char in list('AKQT98765432'):

            lplay_new = list(map(lambda x: x.replace('J', char), lplay))
            play_new = ''.join(lplay_new)
            new_score = get_base_score(play_new) + get_added_score(play, conv2)
            tries.append(new_score)

        return max(tries)

    else:
        return get_score(play, conv2)


def part1():

    with open(path, 'r') as f:

        lines = f.read().split('\n')

        plays = [line.split()[0] for line in lines]
        bids = [int(line.split()[1]) for line in lines]
        scores = [get_score(play, conv) for play in plays]

        _, s_bids  = zip(*sorted(zip(scores, bids)))

        ranks = np.arange(1, 1+len(scores))
        wins = [rank * bid for rank, bid in zip(ranks, s_bids)]

        print(sum(wins))


def part2():

    with open(path, 'r') as f:

        lines = f.read().split('\n')

    plays = [line.split()[0] for line in lines]
    bids = [int(line.split()[1]) for line in lines]
    scores = [get_score_2(play) for play in plays]

    _, s_bids = zip(*sorted(zip(scores, bids)))

    ranks = np.arange(1, 1+len(scores))
    wins = [rank * bid for rank, bid in zip(ranks, s_bids)]

    print(sum(wins))


if __name__ == '__main__':

    part1()
    part2()