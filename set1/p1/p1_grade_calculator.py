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
            view_results(grades)
        elif choice == "X":
            break
        else:
            print("\nInvalid input. Please enter (A, B, or X) only.\n")

def enter_grades():
    
    while True:
        text = input("\nEnter how many grades do you want to compute? ")
        if text.isdigit() and int(text) > 0:
            break
            
        print("\nInvalid input. Please enter a whole number greater than 0.\n")

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

        print("\nInvalid grade. Enter a number from 0 to 100.\n")

Passing_Grade = 75

def get_highest(grades):
    return max(grades)

def get_lowest(grades):
    return min(grades)

def compute_average(grades):
    return sum(grades) / len(grades)

def get_status(grades, passing = Passing_Grade):
    if compute_average(grades) >= passing:
        return "YOU HAVE PASSED!"
    return "YOU HAVE FAILED!"

def view_results(grades):
    if not grades:
        print("\nNotice: Choose A to enter your grades.")
        return

    average = compute_average(grades)
    print("\n====== THIS IS YOUR RESULT ======\n")
    print("Grades  :", grades)
    print("Highest Grade :", get_highest(grades))
    print("Lowest Grade :", get_lowest(grades))
    print("Your Average :", average)
    print("Your Status  :", get_status(grades))

main()

# ========= Explanation of Local and Global Variables =========== #

# In my opinion, the difference between a local and a global variable is that local variables are created within a function and therefore can be accessed only within that function.
# The variables grades in main() and average in view_results() are local variables from my code, while, a global variables are created outside any function and can be accessed by any function in the program.
# Passing_Grade in my code is a global variable and it’s accessed by get_status().