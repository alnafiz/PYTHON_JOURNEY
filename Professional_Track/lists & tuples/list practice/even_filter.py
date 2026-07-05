mixed_numbers = [12, 7, 9, 24, 35, 42, 5]
even_numbers = []

for num in mixed_numbers:
    
    if num % 2 == 0:
        even_numbers.append(num)

print("List of only even numbers:", even_numbers)