# Lab 1 Part 3
import re

# function to convert a string into camelCase
def camelCase(snake_str):
   # components = snake_str.split(' ')
    # capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
  #  return components[0] + ''.join(x.title() for x in components[1:])
# This code taken from stacked overflow but the original splits it based on "_" 
# and I changed it to work with a ' ' (blank space) to work for this instance

    title_case = snake_str.title() # Uppercase first letter of each word
    upper_camel_cased = title_case.replace(' ', '') 
	# Lowercase first letter, join with rest of string 
	# Slices don't produce index out of bounds errors. 
	# So this still works on empty strings, strings of length 1
    return upper_camel_cased[0:1].lower() + upper_camel_cased[1:] 


def main():
    string = input('Enter a string you want to turn into camelcase: ')
    print(camelCase(string))


if __name__ == '__main__':
    main()
