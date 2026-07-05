prices = [150, 450, 299, 799, 120]

largest = prices[0]

for p in prices:
    if p > largest:
        largest = p

print("Largest number:", largest)