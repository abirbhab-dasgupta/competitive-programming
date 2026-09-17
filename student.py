n= int(input("Enter number of students: "))
students = []
for i in range(n):
    name  = input(f"Enter student name {i+1} : ")
    students.append(name)
search_name = input("Enter student name to search: ")
found = False
for i in range(n):
    if students[i] == search_name:
        print("\nCase-sensitive search:")
        print("Student found at position:",i+1)
        found = True
        break
if not found:
    print("\nCase-sensitive search:")
    print("Student not found at position:",n+1)
found = False

for i in range(n):
    if students[i].lower() == search_name.lower():
        print("\nCase-sensitive search:")
        print("Student found at position:",i+1)
        found = True
        break
if not found:
    print("\nCase-sensitive search:")
    print("Student not found at position:",n+1)
