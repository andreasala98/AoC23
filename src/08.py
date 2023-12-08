import os, pathlib
import numpy as np
from math import lcm

path = os.path.join(pathlib.Path(__file__).parent.parent, 'data', '08.in')

def Pbc(i, tot):
    while i>=tot:
        i = i - tot
    while i < 0:
        i = i + tot
    return i

def part1():

    with open(path, 'r') as f:
        chunks = f.read().split('\n\n')

    instructions = chunks[0]
    roads = chunks[1].split('\n')
    N = len(instructions)

    nodes = [node.split('=')[0].strip() for node in roads]

    dests = [(node.split('=')[1].split(',')[0].strip().strip('('),
              node.split('=')[1].split(',')[1].strip().strip(')')) for node in roads]
    
    lookup = {node: dest for node, dest in zip(nodes, dests)}

    i = 0
    stop  = None
    start = 'AAA'

    while start!='ZZZ':
        looked = lookup[start]
        dir = instructions[Pbc(i, N)]
        start =  looked[0] if dir == 'L' else looked[1]
        i += 1

    print(i)


def part2():
        
    with open(path, 'r') as f:
        chunks = f.read().split('\n\n')

    instructions = chunks[0]
    roads = chunks[1].split('\n')
    N = len(instructions)
    M = len(roads)

    nodes = [node.split('=')[0].strip() for node in roads]

    dests = [(node.split('=')[1].split(',')[0].strip().strip('('),
              node.split('=')[1].split(',')[1].strip().strip(')')) for node in roads]
    
    lookup = {node: dest for node, dest in zip(nodes, dests)}

    starting_nodes = [n for n in nodes if n[-1]=='A']
    looked = [0 for _ in starting_nodes]
    nsteps = []
    for i in range(len(starting_nodes)):
        steps = 0
        current = starting_nodes[i]

        while current[-1]!='Z':
            looked = lookup[current]
            current = looked[0] if instructions[Pbc(steps, N)]=='L' else looked[1]

            steps += 1
        
        nsteps.append(steps)

    print(lcm(*nsteps))



if __name__ == '__main__':
    part1()
    part2()