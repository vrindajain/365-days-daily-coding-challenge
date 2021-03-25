#### Problem 2
# This problem was asked by Uber.
# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?

def get_factors(array):
    totalProduct = 1
    rightAarray = list()
    for num in array:
        totalProduct *= num
        rightAarray.append(totalProduct)

    totalProduct = 1
    leftArray = list()
    for num in array[::-1]:
        totalProduct *= num
        leftArray.append(totalProduct)
    leftArray = leftArray[::-1]

    output_array = list()
    for i in range(len(array)):
        num = None
        if i == 0:
            num = leftArray[i + 1]
        elif i == len(array) - 1:
            num = rightAarray[i - 1]
        else:
            num = rightAarray[i - 1] * leftArray[i + 1]
        output_array.append(num)

    return output_array


print( get_factors([1, 2, 3, 4, 5]) )
print(get_factors([3, 2, 1]))
