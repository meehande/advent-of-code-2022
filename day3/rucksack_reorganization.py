import string

LETTERS = string.ascii_letters

def sum_common_items_priorities(filename: str = "advent-2022/day3/input.txt"):
    summed = 0
    with open(filename, 'r') as f:
        while next_line := f.readline():
            # might need to strip newline char here
            midpoint = len(next_line) // 2

            common = set(next_line[:midpoint]).intersection(next_line[midpoint:])

            summed += LETTERS.index(common.pop()) + 1

    return summed

            
def sum_group_common_item_priorities(filename: str = "advent-2022/day3/input.txt"):
    summed = 0
    with open(filename, 'r') as f:

        group = []
        while next_line := f.readline():
            if next_line.endswith('\n'):
                next_line = next_line[:-len('\n')]
            group.append(next_line)

            if len(group) == 3:
                common = set(group[0]).intersection(group[1]).intersection(group[2])
                summed += LETTERS.index(common.pop()) + 1
                group = []
                
    return summed
