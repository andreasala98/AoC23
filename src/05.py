import os, pathlib

path = os.path.join(pathlib.Path(__file__).parent.parent, 'data', '05.in')

class Converter():

    def __init__(self, data) -> None:

        self.source_ranges = []
        self.dest_ranges = []
        
        for d in data:
            dest, source, step = d

            self.source_ranges.append((source, source+step))
            self.dest_ranges.append((dest, dest+step))
    
    def convert(self, num):

        for i,rng in enumerate(self.source_ranges):
            if rng[0] <= num < rng[1]:
                # print(f"Seed {num} in range {rng}")
                diff = num - rng[0]
                return self.dest_ranges[i][0] + diff 

        #the number is not in any range --> return itself
        return num
    
def get_new_seed_list(seed_list):

    out = []
    for i in range(0, len(seed_list), 2):
        #print(i)
        out.extend([k for k in range(seed_list[i], seed_list[i]+seed_list[i+1])])

    return out




def part1and2():

    with open(path, 'r') as f:

        chunks = f.read().split('\n\n')

    seed_list = chunks[0].split(':')[1].strip().split(' ')
    seed_list = [int(s) for s in seed_list]

    print("Seed list: ", len(seed_list))
    
    seed_soil_map = chunks[1].split(':')[1].strip('\n').split('\n')
    seed_soil_map = [[int(num) for num in s.split(' ')] for s in seed_soil_map ]

    soil_fert_map = chunks[2].split(':')[1].strip('\n').split('\n')
    soil_fert_map = [[int(num) for num in s.split(' ')] for s in soil_fert_map ]

    fert_watr_map = chunks[3].split(':')[1].strip('\n').split('\n')
    fert_watr_map = [[int(num) for num in s.split(' ')] for s in fert_watr_map ]

    watr_lite_map = chunks[4].split(':')[1].strip('\n').split('\n')
    watr_lite_map = [[int(num) for num in s.split(' ')] for s in watr_lite_map ]

    lite_temp_map = chunks[5].split(':')[1].strip('\n').split('\n')
    lite_temp_map = [[int(num) for num in s.split(' ')] for s in lite_temp_map ]

    temp_humi_map = chunks[6].split(':')[1].strip('\n').split('\n')
    temp_humi_map = [[int(num) for num in s.split(' ')] for s in temp_humi_map ]

    humi_loca_map = chunks[7].split(':')[1].strip('\n').split('\n')
    humi_loca_map = [[int(num) for num in s.split(' ')] for s in humi_loca_map ]

    seed2soil = Converter(seed_soil_map)
    soil2fert = Converter(soil_fert_map)
    fert2watr = Converter(fert_watr_map)
    watr2lite = Converter(watr_lite_map)
    lite2temp = Converter(lite_temp_map)
    temp2humi = Converter(temp_humi_map)
    humi2loca = Converter(humi_loca_map)

    locs = []
    locs2 = []

    for seed in seed_list:
        soil = seed2soil.convert(seed)
        fert = soil2fert.convert(soil)
        watr = fert2watr.convert(fert)
        lite = watr2lite.convert(watr)
        temp = lite2temp.convert(lite)
        humi = temp2humi.convert(temp)
        loca = humi2loca.convert(humi)

        locs.append(loca)

    print("Part 1:", min(locs))

    for i in range(0, len(seed_list), 2):

        temp_locs = []
        start = seed_list[i]
        stop = seed_list[i] + seed_list[i+1]
        print(start, "-->", stop)

        for new_seed in range(start, stop):
            soil = seed2soil.convert(new_seed)

            fert = soil2fert.convert(soil)
            watr = fert2watr.convert(fert)
            lite = watr2lite.convert(watr)
            temp = lite2temp.convert(lite)
            humi = temp2humi.convert(temp)
            loca = humi2loca.convert(humi)

            temp_locs.append(loca)

        locs2.append(min(temp_locs))
        # print(f" {seed} {soil} {fert} {watr} {lite} {temp} {humi} {loca}")


    print(min(locs2))

if __name__ == '__main__':

    part1and2()