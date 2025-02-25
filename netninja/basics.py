
# print('getting started!')

# name = input("What do you call yourself?")
# print('Hello there,', name)

# Calculate area of circle
# Inputs are stored as strings and must be converted back
# radius = input('What is the radius of your circle (m)?')
# area = 3.142 * int(radius)**2
# print(area)


# String Formatting
num1 = 3.145678
num2 = 10.29988

# old way: print('Num1:', num1, 'Num2:', num2)
# *************************************
# FORMAT METHOD
# :. precision option on index tells you how many digits you want (not after decimal point)
print('num1 is {0:.3} and num2 is {1:.3}'.format(num1, num2))

# using f gives you to that many digits after the decimal place (rounding if necessary)
print('num1 is {0:.3f} and num2 is {1:.3f}'.format(num1, num2))


#F STRINGS, f goes in front of string to use template literals
print(f'num 1 is {num1:.3} and num 2 is {num2:.3f}')

# *************************************
# IF STATEMENTS

