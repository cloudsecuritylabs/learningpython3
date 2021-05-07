print('How old are you?', end=' ')
age = input()
print('How tall are you?', end=' ')
height = input()
print("what is your weight?", end=' ')
weight = input()

# Print using format
print('You are {} years old, {} inches tall and you weight {} lbs'.format(age, height, weight))

# Print using f
print(f'You are {age} years old, {height} inches tall and {weight} lbs heavy')