# In this program, we are going to pass a file to the argv variable
from sys import argv
script, filename = argv

# Open the file passed from the argv
txt = open(filename)

print(f'The filename you have entered is {filename}')
print(txt.read())

txt.close()

# get another filename to read
print('Type another filename')
file = input('> ')

file_txt = open(file)
print(file_txt.read())
file_txt.close()


