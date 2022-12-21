

def range_within(x0, y0, x1, y1):
    """
    check if (x0, y0) is within (x1, y1)
    true if so
    """
    return (x0 >= x1) and (y0 <= y1)


def number_overlapping_full_ranges(filename: str = "advent-2022/day4/input.txt"):

    n = 0
    with open(filename, 'r') as f:

        while nextpair := f.readline():
            e0, e1 = nextpair.split(',')

            e0_x , e0_y = e0.split('-')

            e1_x , e1_y = e1.removesuffix('\n').split('-')

            e0_x , e0_y, e1_x , e1_y = int(e0_x) , int(e0_y), int(e1_x), int(e1_y)

            if range_within(e0_x , e0_y, e1_x , e1_y) or range_within(e1_x , e1_y, e0_x , e0_y):
                n += 1

    return n


def range_overlap(x0, y0, x1, y1):
    return (x0>=x1 and x0<=y1) or (y0>=x1 and y0<=y1)


def number_overlapping_any(filename: str = "advent-2022/day4/input.txt"):

    n = 0
    with open(filename, 'r') as f:

        while nextpair := f.readline():
            e0, e1 = nextpair.split(',')

            e0_x , e0_y = e0.split('-')

            e1_x , e1_y = e1.removesuffix('\n').split('-')

            e0_x , e0_y, e1_x , e1_y = int(e0_x) , int(e0_y), int(e1_x), int(e1_y)

            if range_overlap(e0_x , e0_y, e1_x , e1_y) or range_overlap(e1_x , e1_y, e0_x , e0_y):
                n += 1

    return n 

