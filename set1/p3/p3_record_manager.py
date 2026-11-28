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
    
main()