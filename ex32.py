
numbers = []

def generate_list(bottom_number, top_number):
    num = bottom_number
    print("num = ", num)
    if num > top_number:
        numbers.append(num)
        increment = input("How much would you like to add this time? ")
        num += int(increment)
        print("Numbers currently: ", numbers)
        generate_list(num, top_number)
        
    return numbers

generate_list(0, 100)