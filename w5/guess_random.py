from pnm import papply
from hnm import happly
from ABgame import scoring
from random import choice

def guess(length = 4, can_repeat = False):
    
    # init possible answers
    possible_ans = []
    if can_repeat:
        happly(10, length, possible_ans.append)
    else:
        papply(10, length, possible_ans.append)


    def list2str(g):
        return("".join(list(map(str, g))))

    # input alert
    print("=============================")
    print(" Input example:")
    print("     \"1 2\" stands for 1A2B ")
    print("     \"0 0\" stands for 0A0B ")
    print("     \"4 0\" stands for 4A0B ")
    print("=============================")

    # start guessing
    last_res = (0, 0)
    while not last_res == (4, 0):
        last_guess = choice(possible_ans)
        last_res = tuple(map(int, input(list2str(last_guess) + "   ?A ?B: ").split()))
        possible_ans = list(filter(lambda x: scoring(last_guess, x) == last_res, possible_ans))
        if len(possible_ans) == 0:
            print("No answers left. Did you input correctly?")
            return
        
guess()
