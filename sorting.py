# Given an array of dicts, sort them by a particular key: That key will be a number.
# e.g. Input:
# [
# {a: 14234, b: 1},
# {a: 11232, b: 1},
# {a: 1, b: 1},
# {a: 12, b: 2},
# {a: 16, b: 2},
# {a: 19, b: 3},
# {a: 1123, b: 6}
# ]

# Implement a function which will take input and key as an argument an then sort the array.
# For example, your function
# name is sort_array, if I call sort_array(input, 'a'),
# it will bring objects with smaller value in a first. Output should
# look like this

# [
# {a: 1, b: 1},
# {a: 12, b: 2},
# {a: 16, b: 2},
# {a: 19, b: 3},
# {a: 1123, b: 6},
# {a: 11232, b: 1},
# {a: 14234, b: 1},
# ]
input_arr = [
    {'a': 14234, 'b': 1},
    {'a': 11232, 'b': 1},
    {'a': 1, 'b': 1},
    {'a': 12, 'b': 2},
    {'a': 16, 'b': 2},
    {'a': 19, 'b': 3},
    {'a': 1123, 'b': 6}
]


def sort_array(l1, key):
    for i in range(len(l1)):
        for j in range(i + 1, len(l1)):
            c = 0
            if l1[i][key] > l1[j][key]:
                c = l1[i]
                l1[i] = l1[j]
                l1[j] = c
            else:
                continue
    return l1


input_copy = input_arr.copy()
l2 = sort_array(input_copy, 'a')
print(l2)
print(input_arr)
