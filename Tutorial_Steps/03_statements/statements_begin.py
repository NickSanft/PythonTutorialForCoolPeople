"""
Objective: Loop through the number 1 through 10 and print whether each number is odd or even

Ah, statements. The thing everyone knows from movies and TV.

Here are groups we'll focus on.

1) If, elif, and else.

The syntax is not too bad:

if statement_is_true:
[indent] do_something
elif statement_is_true:
[indent] do_something_else
else:
[indent] do_something_if_everything_else_fails

***Important - in Python, True or False can also be 1 or 0. This is very important for the objective!***

2) for loops

We will just focus on looping through numbers

for [variable_name] in range([start],[end]:
[indent] do_something

The last and trickiest part to know - the % sign.
When used as a statement for two numbers, it will check to see if there would be a remainder if they were divided.
This returns 1 if there would be a remainder, and 0 if there will not.

Try it like this!
print(5 % 2)

With all of that info, you can now tackle the objective!
"""

fav_number = 3

if fav_number < 0:
    print("Hey, you can't have a negative number!")
elif fav_number == 3:
    print("I'm a favorite number!")
else:
    print("I'm not a favorite number!")

for number in range(1, 11):
    print(number)
