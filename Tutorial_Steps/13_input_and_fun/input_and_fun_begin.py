"""

Objective - Install the pyttsx3 module, run it, then have some fun :)

We will talk about one more built-in function in Python - input. When this function is called, the program will wait for
you to type something in before continuing on. Try typing your name and see what happens

To install pyttsx3, you can use pip. Check out the install_modules section if you need a refresher.

"""

import pyttsx3

name = input("What is your name?")

tts = pyttsx3.init()
message_to_say = "Hello {}".format(name)
print("Saying: {}".format(message_to_say))
tts.say(message_to_say)
tts.runAndWait()
