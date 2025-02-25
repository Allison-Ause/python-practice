import operator

operators = {
  "Add": operator.add,
  "Subtract": operator.sub,
  "Multiply": operator.mul,
  "Divide": operator.truediv
}

def calculator():
  print("Enter a number:")
  num1 = int(input())
  print("Enter a second number:")
  num2 = int(input())
  print("What do you want to do to these numbers? \n Your options are: \n Add \n Subtract \n Multiply \n Divide")
  method = input()

  if operators[method]:
    solution = operators[method](num1, num2)
    print("Your solution is:", solution)
  else:
      "Please select a valid operation."
# method = input()
# if method == 'Add':
#     method = '+'
#     print("+")
# elif method == 'Subtract':
#     method = '-'
#     print("-")
# elif method == 'Multiply':
#     method = '*'
#     print("*")
# elif method == 'Divide':
#     method = '/'
#     print("/")
# else:
#     print("Please select a valid option")
#     method = input()
#     print("try again")
# solution = eval("num1 method num2")
# print("Your answer is:", solution)