print "How many numbers would you like to add?"
number_of_numbers = raw_input(">>> ")

print "What are these numbers?"
actual_numbers = raw_input(">>> ")

def adding_some_numbers(actual_numbers, number_of_numbers):
    
    actual_numbers = actual_numbers.split()
    sum = 0
    # if range(len(actual_numbers)) = number_of_numbers

    for number in range(int(number_of_numbers)):
        sum = sum + int(actual_numbers[number])
    return sum

print adding_some_numbers(actual_numbers, number_of_numbers)