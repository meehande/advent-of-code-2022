import pandas as pd
import heapq

def find_max_cals(filename: str = 'advent-2022/day1/input.txt'):
    max_cals = 0
    with open(filename, 'r') as f:
        curr_elf_cals = 0
        for line in f:
            if line.strip('\n') == '':
                # next elf coming
                if curr_elf_cals > max_cals:
                    max_cals = curr_elf_cals
                curr_elf_cals = 0
            else:
                curr_elf_cals += int(line.strip('\n'))
    print(f'max cals: {max_cals}')
    return max_cals
            

find_max_cals()


def find_top_3_cals(filename: str = 'advent-2022/day1/input.txt'):
    with open(filename, 'r') as f:
        cals = []


        curr_elf_cals = 0
        for line in f:
            if line.strip('\n') == '':
                # next elf coming
                cals.append(curr_elf_cals)
                curr_elf_cals = 0
            else:
                curr_elf_cals += int(line.strip('\n'))
    print(f'top 3 max cals: {cals[-3:]}')
    max_cals = sum(sorted(cals[-3:]))
    return max_cals
