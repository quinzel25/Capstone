# Lab 1 Part 3
import re


string = input('Enter a string you want to turn into camelcase: ')

# function to convert a string into camelCase
def camelCase(snake_str):
    components = snake_str.split(' ')
    # capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return components[0] + ''.join(x.title() for x in components[1:])
# This code taken from stacked overflow but the original splits it based on "_" 
# and I changed it to work with a ' ' (blank space) to work for this instance


print(camelCase(string))

  
