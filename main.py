import sys
from time import sleep

def typing_function(name):
 words = f"Hello {name}"
 for char in words:
    sleep(0.25)
    sys.stdout.write(char)

name = "What is your name?"

typing_function(name)
# ^^^ function to make text appear as its being typed ^^^








