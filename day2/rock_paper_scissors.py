OPPONENT_MAP = {
    "A": 1, # ROCK 
    "B": 2, # PAPER
    "C": 3, # SCISSORS
}
MY_MAP = {
    "X": 1, # ROCK 
    "Y": 2, # PAPER
    "Z": 3, # SCISSORS
}

VICTORS = {
    1: 3, # ROCK BEATS SCISSORS
    2: 1, # PAPER BEATS ROCK
    3: 2 # SCISSORS BEATS PAPER
}

LOSERS = {
    v:k for k, v in VICTORS.items()
}


def calculate_score_wrong(filename: str = "advent-2022/day2/input.txt"):
    with open(filename, 'r') as f:
        my_score = 0
        for line in f:
            opp_sym, me_sym = line.strip('\n').split(' ')
            opp_shape = OPPONENT_MAP[opp_sym]
            my_shape = MY_MAP[me_sym]
            
            if opp_shape == my_shape:
                outcome = 3 # draw
            elif opp_shape == VICTORS[my_shape]:
                outcome = 6 # win 
            else:
                outcome = 0 # lose
            my_score += (my_shape + outcome)
    print(f'My Score: {my_score}')      
    return my_score      


OUTCOME_MAP = {
    "X": (lambda opp_shape: VICTORS[opp_shape], 0), # LOSE - 0
    "Y": (lambda opp_shape: opp_shape, 3), # DRAW
    "Z": (lambda opp_shape: LOSERS[opp_shape], 6), # WIN
}

def decrypt_and_calculate_score(filename: str = "advent-2022/day2/input.txt"):
    with open(filename, 'r') as f:
        my_score = 0
        for line in f:
            opp_sym, outcome_sym = line.strip('\n').split(' ')
            my_shape_fn, outcome = OUTCOME_MAP[outcome_sym]
            opp_shape = OPPONENT_MAP[opp_sym]
            my_shape = my_shape_fn(opp_shape)
            my_score += (my_shape + outcome)
        print(f'My Score: {my_score}') 




