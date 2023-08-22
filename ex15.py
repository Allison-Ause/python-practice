
# this tells python to pull in arguments
from sys import argv

# this expands and defines the variables contained within argv
script, filename = argv
#this defines txt as the file object returned from open method (has .read() and .close() available for it)
txt = open(filename);

#this prints the name of the file
print(f"Here's your file {filename}: ");
#this prints the contents of the file
print(txt.read());
# always close file after opening
txt.close();

print("Type the filename: ");
file_again = input("> ");

txt_again = open(file_again);

print(txt_again.read());
txt_again.close();

