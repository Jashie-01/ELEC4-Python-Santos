# Full Name: Jasmine De Leon Santos
# Section: IV-BSIT-B
# Activity: P2 - Custom Module: student_utils
# Date: November 27,2026

import student_utils                    #importing module
from student_utils import get_status    #from module import name
import random                           #built-in module for random message

count = int(input("\nEnter how many grades do you want to compute? "))
grades = []
for n in range(1, count + 1):
    grade = int(input(f"Grade {n}: "))
    grades.append(grade)

average = student_utils.compute_average(grades)
highest = student_utils.get_highest(grades)
lowest = student_utils.get_lowest(grades)
status = get_status(grades)

if status == "YOU HAVE PASSED!":
    message = random.choice(["You did it, Congratulations!"]) # A built-in module (Message)
else:
    message = random.choice(["Don't give up! kaya mo yan tiwala lang, keep fighting!"]) # A built-in module (Message)

print("\n====== THIS IS YOUR RESULT ======\n")
print("Grades  :", grades)
print("Highest :", highest)
print("Lowest  :", lowest)
print("Your Average :", average)
print("Your Status  :", status)
print("Message :", message)