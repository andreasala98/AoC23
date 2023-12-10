import os, pathlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.path as mpath

path = os.path.join(pathlib.Path(__file__).parent.parent, 'data', '10.in')
DIRS = ['N', 'E', 'S', 'W']

class Node(object):

    def __init__(self, pos, letter) -> None:
        
        self.pos = pos
        self.letter = letter
        self.dirs = []

        if self.letter == '|':
            self.dirs = ['N', 'S']
        elif self.letter == '-':
            self.dirs = ['W', 'E']
        elif self.letter == 'J':
            self.dirs = ['W', 'N']
        elif self.letter == 'F':
            self.dirs = ['S', 'E']
        elif self.letter == 'L' or self.letter=='S':
            self.dirs = ['N', 'E']
        elif self.letter == '7':
            self.dirs = ['W', 'S']

    def __repr__(self) -> str:
        return self.letter
    
    def __eq__(self, __value: object) -> bool:
        return self.letter == __value.letter
        

def opposite(dir):

    if dir=='N':
        return 'S'
    elif dir=='S':
        return 'N'
    elif dir=='E':
        return 'W'
    elif dir=='W':
        return 'E'
    return -1


def find_next(node: Node, prev_node: Node):

    pos_diff = (node.pos[0]-prev_node.pos[0], node.pos[1] - prev_node.pos[1])
    if pos_diff == (0, 1):
        incoming_dir = 'W'
    elif pos_diff == (0, -1):
        incoming_dir = 'E'
    elif pos_diff == (1, 0):
        incoming_dir = 'N'
    else:
        incoming_dir = 'S'

    free_dir = [d for d in node.dirs if d != incoming_dir][0]

    next_pos = ''
    if free_dir == 'S':
        return (node.pos[0]+1, node.pos[1])
    elif free_dir == 'N':
        return (node.pos[0]-1, node.pos[1])
    elif free_dir == 'W':
        return (node.pos[0], node.pos[1]-1)
    elif free_dir == 'E':
        return (node.pos[0], node.pos[1]+1)
    
    return next_pos



def part1and2():

    out2 = 0

    with open(path, 'r') as f:

        lines = f.read().split('\n')

        letter_grid = np.asarray([list(line) for line in lines])

    node_grid = np.asarray([[Node((j,i), letter_grid[j,i]) for i in range(len(letter_grid))] for j in range(len(letter_grid[0]))])



    start_pos = np.argwhere(node_grid == Node((-1, -1), 'S'))[0]
    start_pos = (start_pos[0], start_pos[1])
    print(f"Source position: {start_pos}")
    start_node = node_grid[start_pos]

    next_pos = (start_pos[0], start_pos[1]+1)
    next_node = node_grid[next_pos]

    # print(start_node, end=' ')
    # print(next_node, end = ' ')

    pth = [start_node, next_node]

    while next_node.letter != 'S':
        next_pos = find_next(next_node, start_node)

        start_node = next_node
        next_node = node_grid[next_pos]

        pth.append(next_node)
        #print(next_node.letter, end=' ')


    max_distance = (len(pth)-1)//2
    print()
    print(max_distance)

    # #part 2
    # ans_2 = 0
    # inside = []

    # poly = [node.pos for node in pth[:-1]]
    # p = mpath.Path(poly)
    # for y in range(len(node_grid)):
    #     for x in range(len(node_grid[0])):
    #         if [x, y] in poly:
    #             continue
    #         if p.contains_point((x, y)):
    #             ans_2 += 1
    #             inside.append((x,y))

    # print(ans_2)
    # breakpoint()

    # inside = []

    # poly = mpath.Path([list(vert.pos) for vert in pth])

    # for i in range(len(node_grid)):
    #     for j in range(len(node_grid[0])):
    #         if poly.contains_point(node_grid[j,i].pos) and node_grid[j,i] not in pth:
    #             print(f"{node_grid[j,i].pos} inside")
    #             inside.append(node_grid[j,i].pos)
    #             out2 += 1

    # print(out2)


    ct = 0
    print(path)

    for i in range(len(letter_grid)):
        parity = False
        for j in range(len(letter_grid[0])):
            if (i,j) in [p.pos for p in pth]:
                if letter_grid[i,j] in "|JLS":
                    parity = not parity
            else:
                ct += parity
    print(ct)


    # #plotting
    
    pathgrid = np.zeros(letter_grid.shape)
    for i,pair in enumerate(pth):
        pathgrid[pair.pos] = 0.25 + i / len(pth)

    plt.imshow(pathgrid.T)
    plt.scatter(start_pos[0], start_pos[1], marker='*', c='r')
    plt.show()

if __name__ == '__main__':

    part1and2()