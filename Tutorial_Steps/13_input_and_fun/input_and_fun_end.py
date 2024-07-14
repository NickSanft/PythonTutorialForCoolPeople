"""

You had fun, I hope.

"""

import pyttsx3

name = input("What is your name?")

tts = pyttsx3.init()
message_to_say = "Hello {}".format(name)
print("Saying: {}".format(message_to_say))
tts.say(message_to_say)
tts.runAndWait()