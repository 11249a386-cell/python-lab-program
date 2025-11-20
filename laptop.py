def print_details(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

print_details(name="Eve", city="New York")
print_details(product="Laptop", price=1200, brand="Dell")
