#!/usr/bin/python3
def best_score(a_dictionary):
    score = -999999999999999
    score_key = None
    if not a_dictionary:
        return None
    for k, v in a_dictionary.items():
        if v > score:
            score = v
            score_key = k
    return score_key
