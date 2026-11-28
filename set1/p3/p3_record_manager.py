# Full Name: Jasmine De Leon Santos
# Section: IV-BSIT-B
# Activity: P3 - Student Record Manager
# Date: November 28,2026

def show_menu():
    print("\n====== STUDENT RECORD MANAGER ======\n")
    print("(A) Add")
    print("(B) Remove")
    print("(C) Search")
    print("(D) Display/Show Students")
    print("(X) Exit")

def main():
    students = set()
    while True:
        show_menu()
        choice = input("\nWhat would you like to do? (Enter a letter A, B, C, D, or X): ")
        if choice == "A":
            add_student(students)
        elif choice == "B":
            remove_student(students)
        elif choice == "C":
            search_student(students)
        elif choice == "D":
            display_students(students)
        elif choice == "X":
            break
        else:
            print("\nInvalid input. Please enter (A, B, C, D, or X) only.")


def add_student(students):                              # function of adding a student
    name = input("\nEnter a student: ").title()

    if name == "":
        print("\nNo name entered.")
    elif name in students:
        print("\n>> Notice: Duplicate names cannot be added.")
    else:
        students.add(name)
        print(f"\n>> {name} was added.")


def remove_student(students):                          # function of removing a student
    name = input("\nEnter a student you want to remove: ").title()

    if name in students:
        students.remove(name)
        print(f"\n>> {name} has been removed.")
    else:
        print("\n>> Student you entered was not on the list.")


def search_student(students):                         # function of searching a student
    keyword = input("\nEnter a student you want to search: ").lower()
    found = []

    for name in sorted(students):
        if keyword in name.lower():
            found.append(name)

    if keyword == "" or len(found) == 0:
        print("\n>> Student you entered was not found.")
    else:
        print("\nSearch results:")
        for name in found:
            print(">>", name)


def display_students(students):
    if len(students) == 0:
        print("\n>> No students yet on the list.")
        return

    print("\n========== STUDENT LIST ==========\n")
    number = 1

    print(f"Total number of students: {len(students)}\n")

    for name in sorted(students):
        print(f"{number}. {name}")
        number = number + 1

main()

# The list maintains the order as the elements get inserted, and there may be duplicate elements within the list. 
# However, a set has no order maintained within it and does not allow duplicates. 
# I used a set named students to keep the names so that no name would be repeated. I used a list named found for matching names.