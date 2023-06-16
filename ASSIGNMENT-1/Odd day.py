numbers = input("Enter a series of numbers (separated by spaces): ")
numbers_list = numbers.split()

even_count = 0
odd_count = 0

for number in numbers_list:
    number = int(number)
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)