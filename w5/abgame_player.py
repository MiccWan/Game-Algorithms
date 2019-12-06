from pnm import papply
from hpnm import hpapply
from ABgame import scoring

worst_steps = 0
hardest_secret = [0,0,0,0]
total_steps = 0

def autoGuess(secret, length = 4, can_repeat = False, max_num = 10, DEBUG = False):
    
    # print("Now tring to guess", secret)

    # init possible answers
    possible_ans = []
    if can_repeat:
        hpapply(max_num, length, possible_ans.append)
    else:
        papply(max_num, length, possible_ans.append)
    all_ans = possible_ans.copy()
    if DEBUG:
        print("finished init possible_ans", possible_ans)
        print(len(possible_ans))

    # return a filtered result after a guess
    def possible_ans_filtered_by_a_guess(possibilities, guess, result):
        return(list(filter(lambda x: scoring(guess, x) == result, possibilities)))

    # return the min number that an answer can remove from possible answer
    def eval_a_guess(g):
        ab_cnt = dict()
        for ans in possible_ans:
            guess_result = scoring(g, ans)
            ab_cnt[guess_result] = ab_cnt.get(guess_result, 0) + 1
        if DEBUG:
            print("evaling", g, "return with", -max(ab_cnt.values()))
            # print(ab_cnt)
            # print(max(ab_cnt.values()))
        # return the group size with max number(negative)
        return(-max(ab_cnt.values()))

    # generate a guess by Knuth's algorithm
    def get_choice(all_ans, possible_ans):
        best = -len(possible_ans)
        if best == -1:
            return possible_ans[0]
        should_guess = 0
        for ans in all_ans:
            ans_score = eval_a_guess(ans)
            if ans_score > best:
                if DEBUG:
                    print("if guess", ans, "the score will be", ans_score, "which is better.")
                best = ans_score
                should_guess = ans
        return(should_guess)


    def list2str(g):
        return("".join(list(map(str, g))))

    # start guessing
    last_res = (0, 0)
    is_first_guess = True
    steps = 0
    while not last_res == (length, 0):
        # decide what to guess
        if is_first_guess:
            # User may input the first guess
            last_guess = [0,0,0,0]
            is_first_guess = False
        else:
            last_guess = get_choice(all_ans, possible_ans)
        steps += 1
        last_res = scoring(last_guess, secret)
        if DEBUG:
            print("Guessed", last_guess)
            print("Get result", last_res)
        # eliminate the possible answers with the last result
        possible_ans = list(filter(lambda x: scoring(last_guess, x) == last_res, possible_ans))
        if DEBUG:
            print("There are {} answers left.".format(len(possible_ans)))
        if len(possible_ans) == 0:
            print("No answers left. Did you input correctly?")
            return
    print("Guessing {} used {} steps.".format(secret, steps))

    # record the worst situation
    global worst_steps, hardest_secret
    if worst_steps < steps:
        worst_steps = steps
        hardest_secret = secret
        print("New record! Guessing {} used {} steps.".format(secret, steps))
    global total_steps
    total_steps += steps

# Example for play once
autoGuess([0,4,3,4], can_repeat=True, max_num = 6, DEBUG = True)

# hpapply(6, 4, lambda l: autoGuess(l, can_repeat = True, max_num = 6))
# print("In the worst situation, guessing {} uses {} steps.".format(hardest_secret, worst_steps))
# print("In average, it use {} steps.".format(total_steps/1296))