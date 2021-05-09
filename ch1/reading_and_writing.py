# in this program, we will pass the filename using argv parameter.
# we will open the file, and then write content
# content will be provided by the end user
from sys import argv
script, filename = argv

print(f'First we will erase content of the file {filename}')
print('to exit, enter ctrl+c')
print('to continue, hit enter')

input('?')

print('Time to open the file ..')
file_obj = open(filename, 'w')

print('Deleting the file content')
file_obj.truncate()

print('Now enter three lines')
line1 = input("line 1 : ")
line2 = input("line 2 : ")
line3 = input("line 3 : ")


print('Now time to write lines to the file')

file_obj.write(line1)
file_obj.write('\n')
file_obj.write(line2)
file_obj.write('\n')
file_obj.write(line3)
file_obj.write('\n')

file_obj.close()
