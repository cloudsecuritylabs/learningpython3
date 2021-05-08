# To pass multiple values via commandline, we can use 'argv' module
# in this code, we are passing three variable to the "script"
# run this program from the commandline
from sys import argv
script, first, second, third = argv
print('the script is ', script)
print('the first is', first)
print('the second is', second)
print('the third is', third)

print(int(first) * int(second) * int(third))