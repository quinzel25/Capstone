## warmup 2 

classes = input('How many classes are you taking? ')
classes = int(classes) 
print(classes)

list1 = []
for x in range(classes):
    stuff = input('Enter name of the class: ')
    list1.append(stuff)

print(list1)