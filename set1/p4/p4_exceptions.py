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

main()