#### Problem 1
# Given a list of numbers, return whether any two sums to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?




def check_sum(array, k):
    potential_solutions = set()

    for num in array:
        if num in potential_solutions:
            return True
        potential_solutions.add(k - num)

    return False


print(check_sum([10, 15, 3, 7], 17))
print(check_sum([10, 15, 3, 4], 17))
print(check_sum([10, 15, 3, 7], 22))
