# import sys
# from time import sleep
#
# def typing_function(name):
#  words = f"Hello {name}"
#  for char in words:
#     sleep(0.25)
#     sys.stdout.write(char)
#
# name = "What is your name?"
#
# typing_function(name)
# ^^^ function to make text appear as its being typed ^^^


def format_name(f_name , l_name):
    f_name.title()
    l_name.title()
    print(f"Hello, {f_name} {l_name}")


first = input("Whats is your first name?")
last = input("Whats is your last name?")
format_name(f_name=first , l_name=last)




