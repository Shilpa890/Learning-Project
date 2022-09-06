# # Given an array of integers, find the second largest number in the array.
# # Input: [1,5,2,8,3,9,5,8,54,36,79,91,84]
# # Output: 84
#
# # def find_second_highest(arr):
# #     return 0
#
#
# input_arr = [1, 5, 2, 8, 3, 9, 995, 8, 54, 36, 79, 84, 91]
# # answer = find_second_highest(input_arr)
# # print('output is {}'.format(answer))
# maxm=1
# secondmax=0
#
# # 1. Number > max [Replace max with new number, second max with old max]
# # 2. Number < max and Number > secondmax [Replace second max with new number]
# # 3: Number < secondmax [Do nothing]
# for x in input_arr:
#     if x>maxm:
#         secondmax=maxm
#         maxm=x
#     elif x<maxm and x>secondmax:
#         secondmax=x
# print(maxm)
# print(secondmax)


# We have a binary array: [1,1,0,1,1,0,1,0,0,0,1,0]
# We have to sort it in most efficient way.
# we have two pointers i and j
# if i=1 and j=0 then i=j, both move i++,j--
# if i=0 and j=1 then i++, both move i++,j--
# if i=1 and j=1 then stop i and let j move j-- till j=0 then move to condition 1
# if i=0 and j=0 then stop j and move i i++ till i=1 then move to condition 2

# arr=[1,1,0,1,1,0,1,0,0,0,1,0]
# i=0
# j=len(arr)-1-i
# while i!=j-1:
#     c=0
#     print("i =",i)
#     print("j =",j)
#     print("arr[j]=" ,arr[j])
#     if arr[i]==1 and arr[j]==0:
#         c=arr[j]
#         arr[j]=arr[i]
#         arr[i]=c
#         i=i+1
#         j=j-1
#     elif arr[i]==0 and arr[j]==1:
#         i=i+1
#         j=j-1
#     elif arr[i]==1 and arr[j]==1:
#         j=j-1
#     elif arr[i]==0 and arr[j]==0:
#         i=i+1
# print(arr)

# given an array of integers from 1 to n .There is a number missing from the array
# eg for n=6
#     input[1,2,3,4,6]
# output should be 5
# solution should ne O(n)
# arr=[1,2,3,4,6]
# for i in range(1,len(arr)+1):
#     if i not in arr:
#         print(i)

# effiecnt method

def miss_n(arr):
    n = len(arr) + 1
    sn = int((n*(n + 1) )/ 2)
    print(sn)
    num = 0
    for num in arr:
        num = num + 1
    return sn - num


l1=[1,4,3,5]
miss_n(l1)

i