# Lab 1 Part 1

name = input('What is your name? ')
birthday_month = input('What month where you born in? ')
#print f is formatting in order to use {variable_name} in code
print(f'Hello, {name}, I hope you\'re having a lovely day')

if birthday_month.lower() == 'january':
    print('Happy birthday month!')

#len counts the amound of characters in the varable
print(f'Your name has {len(name)} letters in it.') 