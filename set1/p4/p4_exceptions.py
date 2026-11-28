# Full Name: Jasmine De Leon Santos
# Section: IV-BSIT-B
# Activity: P4 - Safe Menu Program
# Date: November 28,2026

def show_menu():
    print("\n====== SAFE MENU PROGRAM ======\n")
    print("(A) Division")
    print("(B) Open file")
    print("(X) Exit")

def main():
    while True:
        show_menu()
        choice = input("\nWhat would you like to do? (Enter a letter A, B, or X): ")
        if choice == "A":
            divide_numbers()
        elif choice == "B":
            open_file()
        elif choice == "X":
            break
        else:
            print("\n>> Invalid input. Please enter (A, B, or X) only.")


def divide_numbers():                               # function for dividing two numbers with exception
    try:
        number1 = float(input("\nEnter your first number: "))
        number2 = float(input("Enter your second number: "))
        result = number1 / number2
    except ValueError:
        print("\n>>Attention: Invalid number!\n")
    except ZeroDivisionError:
        print("\n>>Notice: You cannot divide it by zero.\n")
    else:
        print(f"\n>> {number1} / {number2} = {result}\n")
    finally:
        print(">> Finished.")


def open_file():                                    # function for opening a file with exception
    file_name = input("\nEnter your file name: ")

    try:
        with open(file_name, "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("\n>>Attention: File is missing or was not found!\n")
    else:
        print("\n======= FILE DETAILS =======\n")
        print(content)

main()