# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

numbers = [10, 15, 3, 7, 9, 8]
targetNumber = 17


def is_target_in_sum_of_array(i_target, i_numbers):
    print 'trying to find {} as a sum of any 2 numbers in {}'.format(i_target, i_numbers)

    length = len(i_numbers)
    for x in i_numbers:
        index = i_numbers.index(x) + 1                      # get index for current number and get next number in array

        while index < length:                               # check if index is in range
            if (x + i_numbers[index]) == i_target:          # check if sum is equal to target
                print 'match found', x, i_numbers[index]
            index = index + 1                               # increment index to compare all following numbers in array


if __name__ == '__main__':
    is_target_in_sum_of_array(targetNumber, numbers)
