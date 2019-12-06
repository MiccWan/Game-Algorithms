from ABgame import scoring
from evalAnAlgorithm import evalAnAlgorithm

DEBUG = False

# return the min number that an answer can remove from possible answer
def eval_a_guess(g, possible_ans):
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
def get_choice(possible_ans, all_ans):
    best = -len(possible_ans)
    if best == -1:
        return possible_ans[0]
    if len(possible_ans) == 1296:
        return [1,1,2,2]
    should_guess = 0
    for ans in all_ans:
        ans_score = eval_a_guess(ans, possible_ans)
        if ans_score > best:
            if DEBUG:
                print("if guess", ans, "the score will be", ans_score, "which is better.")
            best = ans_score
            should_guess = ans
    return(should_guess)



import timeit

start = timeit.default_timer()

result = evalAnAlgorithm(get_choice)

stop = timeit.default_timer()

print('Time: ', stop - start)

print(result)

# import json
# with open("evalResult.json", "w") as resFile:
#     json.dump(result, resFile, indent=4, sort_keys=True)