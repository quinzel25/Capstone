# Lab 1 Part 2

classes = input('How many classes are you taking? ')
#changes the input from a string to an int
classes = int(classes) 
# creates empty list
list1 = []
# a loop that loops over how mant classes you entered
for x in range(classes):
    stuff = input('Enter name of the class: ')
    #adds variable you just entered to the list
    list1.append(stuff)

# prints out list
for y in list1:
    print(y)


