from pnm import papply
from hnm import happly
from ABgame import scoring

def guess(length = 4, can_repeat = False):
    
    # init possible answers
    possible_ans = []
    if can_repeat:
        happly(10, length, possible_ans.append)
    else:
        papply(10, length, possible_ans.append)

    # return a filtered result after a guess
    def possible_ans_filtered_by_a_guess(possibilities, guess, result):
        return(list(filter(lambda x: scoring(guess, x) == result, possibilities)))

    # return the min number that an answer can remove from possible answer
    def eval_a_guess(g):
        ab_cnt = dict()
        for ans in possible_ans:
            guess_result = scoring(g, ans)
            ab_cnt[guess_result] = ab_cnt.get(guess_result, 0) + 1
        # return the group size with max number
        return(-ab_cnt[max(ab_cnt)])

    # generate a guess by Bulls and Cows algorithm
    def get_choice():
        best = -len(possible_ans)
        if best == -1:
            return possible_ans[0]
        should_guess = 0
        for ans in possible_ans:
            ans_score = eval_a_guess(ans)
            if ans_score > best:
                best = ans_score
                should_guess = ans
        return(should_guess)


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
    is_first_guess = True
    while not last_res == (length, 0):
        if is_first_guess:
            last_guess = possible_ans[0]
            is_first_guess = False
        else:
            last_guess = get_choice()
        last_res = tuple(map(int, input(list2str(last_guess) + "   ?A ?B: ").split()))
        # print(possible_ans)
        possible_ans = list(filter(lambda x: scoring(last_guess, x) == last_res, possible_ans))
        if len(possible_ans) == 0:
            print("No answers left. Did you input correctly?")
            return

guess(can_repeat=False)