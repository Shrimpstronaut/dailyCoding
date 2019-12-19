# Given an array of integers, return a new array such that each element at index i of the new array
# is the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].


def get_product_of_items_in_array_except_index(numbers):
    index = 0
    result_array = []

    while index < len(numbers):                         # iterate over all elements in given array
        temp_product = 1                                # multiply first element of each pass with 1 instead of 0

        for element in numbers:                         # nested iteration to check and multiply each number
            if index != numbers.index(element):         # check if current number is not ignored
                temp_product *= element

        result_array.append(temp_product)
        index += 1                                      # increment index to continue with next number

    return result_array


if __name__ == '__main__':
    array_input = [1, 2, 3, 4, 5]
    result = get_product_of_items_in_array_except_index(array_input)

    print "input: {} - result: {}".format(array_input, result)
