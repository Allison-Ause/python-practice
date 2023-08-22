from sys import argv

script, filename = argv
#print(f"We're going to erase {filename}")
print(f"We're going to add to {filename}.")
#print("If you don't want that, his CTRL-C (^C).")
#print("If you do want that, hit RETURN.")


input("? ")

print("Opening the file...")
target = open(filename, 'a')
print("Trunctating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines...")
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file.")

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
target.write(f"""
{line1}
{line2}
{line3}
""")

print("And finally, we close it.")
target.close()

newTarget = open(filename)
print(f"Now redisplaying {filename} after your edits")
print(newTarget.read())
response = input("Are you satisfied with your changes? ")
print(f"You responded: {response}.")
newTarget.close()

