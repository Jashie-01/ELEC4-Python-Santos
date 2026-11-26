# Full Name: Jasmine De Leon Santos
# Section: IV-BSIT-B
# Activity: P1 - Student Grade Calculator
# Date: November 26,2026

def show_menu():
    print("\n==== STUDENT GRADE CALCULATOR ====\n")
    print("(A) Enter grades")
    print("(B) View results")
    print("(X) Exit")

def main():
    grades = []  
    while True:
        show_menu()
        choice = input("\nWhat would you like to do? (Enter a letter A, B, or X): ")
        if choice == "A":
            grades = enter_grades()
        elif choice == "B":
            show_results(grades)
        elif choice == "X":
            break
        else:
            print("\n⚠️  Invalid input. Please enter (A, B, or X) only.")

def enter_grades():
    
    while True:
        text = input("\nHow many grades do you want to compute? ")
        if text.isdigit() and int(text) > 0:
            break
            
        print("\n⚠️  Invalid input. Please enter a whole number greater than 0.")

    grades = []
    for n in range(1, int(text) + 1):
        grades.append(get_valid_grade(n))
    return grades

def get_valid_grade(n):
    
    while True:
        user_input = input(f"Grade {n}: ")

        if user_input.isdigit():
            grade = int(user_input)
            if grade >= 0 and grade <= 100:
                return grade

        print("\n⚠️  Invalid grade. Enter a number from 0 to 100.")

main()