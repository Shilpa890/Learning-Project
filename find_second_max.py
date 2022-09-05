# Given an array of integers, find the second largest number in the array.
# Input: [1,5,2,8,3,9,5,8,54,36,79,91,84]
# Output: 84

# def find_second_highest(arr):
#     return 0


input_arr = [1, 5, 2, 8, 3, 9, 995, 8, 54, 36, 79, 84, 91]
# answer = find_second_highest(input_arr)
# print('output is {}'.format(answer))
maxm=1
secondmax=0

# 1. Number > max [Replace max with new number, second max with old max]
# 2. Number < max and Number > secondmax [Replace second max with new number]
# 3: Number < secondmax [Do nothing]
for x in input_arr:
    if x>maxm:
        secondmax=maxm
        maxm=x
    elif x<maxm and x>secondmax:
        secondmax=x
print(maxm)
print(secondmax)





