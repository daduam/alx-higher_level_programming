#!/usr/bin/python3
def weight_average(my_list=[]):
    weighted_sum = sum([score * weight for (score, weight) in my_list])
    total_weights = sum([weight for (_, weight) in my_list])

    if not my_list or total_weights == 0:
        return 0

    return weighted_sum / total_weights
