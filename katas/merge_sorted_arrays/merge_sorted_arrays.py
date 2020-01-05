"""

https://www.interviewcake.com/question/python3/merge-sorted-arrays?course=fc1&section=array-and-string-manipulation

In order to win the prize for most cookies sold, my friend Alice and I are
going to merge our Girl Scout Cookies orders and enter as one unit.

Each order is represented by an "order id" (an integer).

We have our lists of orders sorted numerically already, in lists. Write a
function to merge our lists of orders into one sorted list.

For example:

    my_list     = [3, 4, 6, 10, 11, 15]
    alices_list = [1, 5, 8, 12, 14, 19]

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
print(merge_lists(my_list, alices_list))


"""


def merge_lists(my_list, alices_list):

    result_length = len(my_list) + len(alices_list)
    result = [None] * result_length

    my_idx = 0
    alices_idx = 0
    result_idx = 0

    while my_idx < len(my_list) and alices_idx < len(alices_list):
        if my_list[my_idx] < alices_list[alices_idx]:
            result[result_idx] = my_list[my_idx]
            my_idx += 1
        else:
            result[result_idx] = alices_list[alices_idx]
            alices_idx += 1
        result_idx += 1

    while my_idx < len(my_list):
        result[result_idx] = my_list[my_idx]
        my_idx += 1
        result_idx += 1

    while alices_idx < len(alices_list):
        result[result_idx] = alices_list[alices_idx]
        alices_idx += 1
        result_idx += 1

    return result
