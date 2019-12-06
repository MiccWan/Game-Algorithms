from ABgame import scoring
from hpnm import hpapply
from pnm import papply

# The parameter <algorithm> must take two parameter which are:
#   "possible answers": The remain answers after times of elimination
#   "all answers": The whole possible code pool. (You may take it but not to use.)

def evalAnAlgorithm(algorithm, max_num = 6, length = 4, can_repeat = True):

    print("jizz")

    # init possible_ans and all_ans
    possible_ans = []
    if can_repeat:
        hpapply(max_num, length, possible_ans.append)
    else:
        papply(max_num, length, possible_ans.append)
    all_ans = possible_ans.copy()
    # print(all_ans)

    def list2str(l):
        return("".join(list(map(str, l))))

    dfs_result = {}

    def dfs(possible_ans, depth = 1):

        
        ab_cnt = {}
        # print("Waiting algorithm response...")
        new_guess = algorithm(possible_ans, all_ans)
        print("Generated guess:", new_guess)
        for ans in possible_ans:
            guess_result = scoring(new_guess, ans)
            ab_cnt[guess_result] = ab_cnt.get(guess_result, []) + [ans]

        for key in ab_cnt:
            if key == (length, 0):
                dfs_result[list2str(ab_cnt[key][0])] = depth
            else:
                dfs(ab_cnt[key], depth + 1)
        # return dfs_result
    
    dfs(possible_ans)
    result = dfs_result
    return(result)