

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 'dimes', 3, 'quarters']

for number in the_count:
    print(f"This is the count {number}")

for fruit in fruits:
    print(f"This is the fruit you picked: {fruit}")

for i in change:
    print(f"I got {i}")
  
elements = list(range(0, 6))

for i in range(0, 6):
    print(f"Adding {i} to the list.")
    elements.append(i)

for i in elements:
    print(f"Element was: {i}")

print(elements)