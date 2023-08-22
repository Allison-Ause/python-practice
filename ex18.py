

def print_two(*args):
      arg1, arg2 = args
      print(f"arg1: {arg1}, arg2: {arg2}.")

def print_two_again(arg1, arg2):
      print(f"arg1: {arg1}, arg2: {arg2}.")

def print_one(arg1):
      print(f"arg1: {arg1}.")

def print_none():
      print("This one takes no parameters, so I got nothin'.")

print_two("Allison", "Ause")
print_two_again("Nosilla", "Euse")
print_one("First!")
print_none()