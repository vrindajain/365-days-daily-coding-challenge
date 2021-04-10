#### Problem 9
#This problem was asked by Airbnb.
#Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
#For example, [2, 4, 6, 8] should return 12, since we pick 4 and 8. [5, 1, 1, 5] should return 10, since we pick 5 and 5.


import sys

def get_largest_non_adj_sum(array):
    previous, largest = 0, 0
    for amount in array:
        print("amount: {}; previous: {}; largest: {}".format(amount, previous, largest))
        previous, largest = largest, max(largest, previous + amount)
        print("new_previous: {}; new_largest: {}".format(previous, largest))
    return largest

print(get_largest_non_adj_sum([2, 4, 6, 8]))
print(get_largest_non_adj_sum([5, 1, 1, 5]))
