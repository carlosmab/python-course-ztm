# highest eve


def is_odd(num):
    return num % 2 != 0


def highest_even(num_list):
    highest_even = None
    for num in num_list:
        if is_odd(num):
            continue
        if not highest_even or num > highest_even:
            highest_even = num
    return highest_even


print(highest_even([10, 2, 3, 4, 8, 11]))

