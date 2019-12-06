from collections import Counter
# import timeit

def scoring(guess, secret):

    a_cnt = len([True for i in range(len(guess)) if guess[i] == secret[i]])
    b_cnt = sum((Counter(guess) & Counter(secret)).values()) - a_cnt

    return (a_cnt, b_cnt)


# print(scoring('4415','3446'))
# print(scoring('4415','6414'))
# print(scoring('4415','1144'))
# print(scoring('4415','4244'))

# print(timeit.timeit(lambda:scoring('1122','4521'),number=10000))