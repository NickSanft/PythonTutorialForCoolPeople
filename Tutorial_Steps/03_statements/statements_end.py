for number in range(1, 10):
    if number % 2:
        print("Odd!")
    else:
        print("Even!")

# Fancy version:
for number in range(1, 10):
    if number % 2:
        print("{} is Odd!".format(number))
    else:
        print("{} is Even!".format(number))
