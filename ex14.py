
from sys import argv
script, user_name, vibe = argv;
prompt = 'Sneeze your answer here: ';

print(f"Hi {user_name}, I'm the {script} script.");
print("I'd like to ask you a few questions.");
print(f"Do you like me {user_name}?");
likes = input(prompt);

print(f"Where do you live {user_name}?");
lives = input(prompt);

print(f"What kind of computer do you have {user_name}?");
computer = input(prompt);

print(f"Since your vibe is {vibe}, how are you feeling today?");
mood = input(prompt);

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
You are feeling {mood}, according to your ring.
""");