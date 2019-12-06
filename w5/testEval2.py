from ABgame import scoring
from evalAnAlgorithm import evalAnAlgorithm

# generate a guess by Knuth's algorithm
def get_choice(possible_ans, all_ans):
    return(possible_ans[0])

result = evalAnAlgorithm(get_choice)

import json
with open("evalResult.json", "w") as resFile:
    json.dump(result, resFile, indent=4, sort_keys=True)