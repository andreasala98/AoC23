import os, pathlib

path = os.path.join(pathlib.Path(__file__).parent.parent, 'data', '01.in')


def part1():

    out = 0

    with open(path, 'r') as f:

        for line in f.readlines():
            num = ''.join(c for c in line if c.isdigit())
            add = int(num[0] + num[-1])
            out += add

    print(out)


def part2():

    conv = {
        'one' : 1,    'two': 2,  'three': 3,
        'four': 4,   'five': 5,    'six': 6,
        'seven': 7, 'eight': 8,   'nine' : 9
    }

    with open(path, 'r') as f:

        out = 0

        for line in f.readlines():

            new_line = line.strip('\n')

            for word, dig in conv.items():
                # this was not explained well for mixed cases eightwo
                new_line = new_line.replace(word, word[0]+str(dig)+word[-1])


            num = ''.join(c for c in new_line if c.isdigit())
            add = int(num[0] + num[-1])
            out += add


    print(out)

if __name__ == '__main__':

    part1()
    part2()
