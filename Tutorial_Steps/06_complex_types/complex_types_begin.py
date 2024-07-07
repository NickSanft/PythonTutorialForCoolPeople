"""
Objectives:

    1) Add a string with the value of "good brunch" BETWEEN morning and afternoon.
    2) Remove the "Nick" key from the dictionary.

Additional Info:

OBJECTIVE 1

Way back in part 2, we learned some of the types and how they can be used.

One of these is a list, which is... a list of items.
The syntax is pretty straightforward, you just create a variable with square brackets [].
A list can start as empty as well!

As you try to solve the objective, try starting a new line at the bottom and type:

mylist.

If you're using PyCharm or another good IDE, you should see all the functions a list has, like append.

Google is also a very good option.

OBJECTIVE 2

Another type is a dictionary, which is a list of key-value pairs.
Think of this as a filing cabinet. Each folder has a key, or label but anything can go into the folders.

The syntax is also pretty straightforward, the dictionary is in curly braces, and the

In the example below, the keys are the names of people, and the values are their favorite color.
Notice that keys have to be unique, but values DO NOT.

To get the contents of a specific "folder", you can do that by using .get and passing in the key.

Same as the first objective, looking through the IDE suggestions and Google are your best friends :)

"""

my_list = ["good morning", "good afternoon", "good evening"]
print(my_list)

my_list.append("good night")
print(my_list)

my_dict = {"Jim": "Purple", "Alex": "Red", "Nick": "Purple"}
print(my_dict)
print(my_dict.get("Alex"))
