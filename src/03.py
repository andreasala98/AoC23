import os, pathlib
import numpy as np

path = os.path.join(pathlib.Path(__file__).parent.parent, 'data', '03.in')


def get_neighbours(num_pos_list, Nrows, Ncols):

    neighs = set()

    for pos in num_pos_list:

        if pos[0]!=0:
            if pos[1]!=0:
                neighs.add((pos[0]-1, pos[1]-1))
            if pos[1]!= Nrows-1:
                neighs.add((pos[0]-1, pos[1]+1))
            neighs.add((pos[0]-1, pos[1])) #
            

        if pos[1]!=0:
            neighs.add((pos[0], pos[1]-1))
        if pos[1]!=Nrows-1:
            neighs.add((pos[0], pos[1]+1))
        
        if pos[0]!=Ncols-1:
            neighs.add((pos[0]+1, pos[1])) #
            if pos[1]!=0:
                neighs.add((pos[0]+1, pos[1]-1))
            if pos[1]!=Nrows-1:
                neighs.add((pos[0]+1, pos[1]+1))


    return neighs



def part1and2():

    with open(path, 'r') as f:

        lines = f.read().split('\n')

    Nrows = len(lines)
    Ncols = len(lines[0])
    out = 0
    out2 = 0
    ast_pos = {}

    for j, line in enumerate(lines):

        visited = set()

        for i in range(len((line))):

            number_len = 0
            number_str = ''

            if line[i].isdigit() and i not in visited:

                this_num_pos = []

                number_len += 1
                number_str += line[i]
                visited.add(i)
                this_num_pos.append((j,i))

                if i == Ncols:
                    break
                nxt = line[i+1]

                while nxt.isdigit():
                    number_len += 1
                    number_str += nxt
                    visited.add(i+1)
                    this_num_pos.append((j,i+1))

                    i += 1
                    if i == Ncols-1:
                        break
                    nxt = line[i+1]

                num = int(number_str)
                neighs = get_neighbours(this_num_pos, Nrows, Ncols)
 
                elements = set([lines[n[0]][min(n[1], Nrows)] for n in neighs if not lines[n[0]][min(n[1], Nrows)].isdigit()])
                
                asts = [n for n in neighs if lines[n[0]][n[1]]=='*']
                for ast in asts:
                    if ast not in ast_pos:
                        ast_pos[ast] = [num]
                    else:
                        ast_pos[ast].append(num)
                

                if elements!={'.'}:
                    out += num


    for vals in ast_pos.values():
        if len(vals)==2:
            out2 += vals[0]*vals[1]

    print(out)
    print(out2)

        

if __name__ == '__main__':

    part1and2()