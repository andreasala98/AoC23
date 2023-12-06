import os, pathlib
from tqdm import trange

path = os.path.join(pathlib.Path(__file__).parent.parent, 'data', '06.in')


def get_distance(total_time, wait_time):
    return wait_time * (total_time-wait_time)


def part1():

    with open(path, 'r') as f:

        ts, ds = f.read().split('\n')

    ts = ts.split(':')[-1].strip().split()
    ds = ds.split(':')[-1].strip().split()

    n_times = [sum(1 for j in range(int(ts[i])) if get_distance(int(ts[i]), j) > int(ds[i])) for i in range(len(ts))]

    out = 1
    for n in n_times:
        out *= n

    print(out)


def part2():

    with open(path, 'r') as f:

        ts, ds = f.read().split('\n')

    ts = int(''.join(ts.split(':')[-1].strip().split()))
    ds = int(''.join(ds.split(':')[-1].strip().split()))

    n_ways = sum(1 for i in trange(ts) if get_distance(ts, i)>ds)

    print(n_ways)


if __name__ == '__main__':

    part1()
    part2()