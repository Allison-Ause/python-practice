


#age = input("How old are you? ");
#height = input("How tall are you? ");
#weight = input("How much do you weigh? ");
#print(f"So you are {age} years old, {height} tall and weigh {weight} pounds. What a wonderful human you are!");

from sys import argv
# read the WYSS section for how to run this
script, first, second, twelfth, nonsense = argv
print("The script is called:", script);
print("Your first variable is:", first);
print("Your second variable is:", second);
print("Your third variable is:", twelfth);
print(f"It's all just {nonsense}, really.");
favorite = input(f"What is your favorite {nonsense}? ");
print("Your favorite is: ", favorite);

