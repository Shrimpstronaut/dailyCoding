# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.


def find_missing_int_in_array(input):
    for x in range(1, len(input) + 1):
        if x not in input:
            return x


if __name__ == '__main__':
    input_array_1 = [3, 4, -1, 1]
    input_array_2 = [1, 2, 0]

    assert find_missing_int_in_array(input_array_1) == 2
    assert find_missing_int_in_array(input_array_2) == 3
