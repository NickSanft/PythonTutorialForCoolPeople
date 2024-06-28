"""
Objective: Fix the issue when running and update the function

Alright, now we have an error :(

The solution is problem is fairly simple, but how could we warn others to not make the mistake?

The functions step will help with this, as our function is missing something that would help a lot!
"""


def add_numbers(number_one, number_two):
    num_sum = number_one + number_two
    print(num_sum)
    return num_sum


add_numbers(1, 5)
add_numbers(1, "Jeff")
