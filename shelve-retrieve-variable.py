import shelve
retrieved_name = shelf['name']
retrieved_age = shelf['age']
retrieved_numbers = shelf['favorite_numbers']
retrieved_student_status = shelf['is_student']

print(f"\nRetrieved Name: {retrieved_name}")
print(f"Retrieved Age: {retrieved_age}")
print(f"Retrieved Favorite Numbers: {retrieved_numbers}")
print(f"Retrieved Student Status: {retrieved_student_status}")
