# this program combines input from the commandline and also from user
from sys import argv
script, user_name = argv # from the commad line, you can pass one variable
prompt = '>'

print(f'Hello {user_name}, you are running this script: {script}') # use f- formatter

age = input(f"How old are you? {prompt} ")
height = input(f"How tall are you? {prompt} ")

my_age = 42 #years
my_height = 56 #incles


if int(age) > my_age and int(height) > my_height:
    print(f'You are {int(age)} year old, you are older than I am and you are taller too')
elif int(age) < my_age and int(height) < my_height:
    print(f'You are {int(age)} year old, you are younger than I am and you are shorter too')
elif int(age) < my_age and int(height) > my_height:
    print(f'You are {int(age)} year old, you are younger than I am , but you taller')
else:
    print(f'You are {int(age)} year old, you are older than I am , but you shorter')