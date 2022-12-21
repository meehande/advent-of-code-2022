from typing import List


def read_input(filename: str = 'advent-2022/day5/input.txt'):
    """
    - read each line and store in buffer
    - once hit row with numbers (need to identify, as the one with a blank line after?)
    - parse numbers = number of stacks
    - go back through buffer (in reverse)
    - use len(line with numbers) / n stacks to find spacing
    - parse line by line to store as list of lists list this (top element at end)
        [
            [Z, J, G] # 1
            [Q, L, R, ...] # 2 
        ]

    """
    buffer = []
    with open(filename, 'r') as f:
        while nextline := f.readline():
            if nextline.strip() == '':
                instructions_location = f.tell() # store where the instructions start to continue from there

                return instructions_location, parse_buffer(buffer)
            else:
                buffer.append(nextline)



def parse_buffer(buffer: List[str]):
    numbers = buffer.pop()
    linelen = len(numbers)
    numbers = [int(n) for n in numbers.strip().split(' ') if n !='']
    nstacks = len(numbers)
    spacing = linelen//nstacks

    stacks = [[] for _ in range(nstacks)]
    for _ in range(len(buffer)):
        line = buffer.pop().rstrip()
        j = 0
        for k in range(spacing, linelen+1, spacing):
            if not line[j:k].isspace():
                stacks[ (k //spacing) -1].append(line[j:k].strip())
            j = k
    return stacks


def move_boxes(stacks: List[List[str]], n: int, from_i: int, to_i: int):
    """
    move n elements from stack from_i to stack to_i
    """
    for _ in range(n):
        stacks[to_i].append(stacks[from_i].pop())
    return stacks



def rearrange_stacks(filename: str = 'advent-2022/day5/input.txt'):
    instructions_location, stacks = read_input()

    with open(filename, 'r') as f:
        f.seek(instructions_location)

        while instruction := f.readline():
            instruction = instruction.strip().split(' ')
            nboxes = int(instruction[1])
            from_stack = int(instruction[3])
            to_stack = int(instruction[-1])
            stacks = move_boxes(stacks, nboxes, from_stack-1, to_stack-1)
    
    return ''.join([s[-1].strip('[]') for s in stacks])









        




def restack():
    pass