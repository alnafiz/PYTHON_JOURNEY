names = ["Anik", "Mitu", "Anik", "Rahul", "Mitu", "Sajid"]
unique_names = []

for name in names:
    
    if name not in unique_names:
        unique_names.append(name)

print("List after removing duplicate:", unique_names)