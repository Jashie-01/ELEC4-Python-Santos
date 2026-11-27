# Full Name: Jasmine De Leon Santos
# Section: IV-BSIT-B
# Activity: P2 - Custom Module: student_utils
# Date: November 27,2026

def get_highest(grades):
    return max(grades)

def get_lowest(grades):
    return min(grades)

def compute_average(grades):
    return sum(grades) / len(grades)

Passing_Grade = 75

def get_status(grades, passing=Passing_Grade):
    if compute_average(grades) >= passing:
        return "YOU HAVE PASSED!"
    return "YOU HAVE FAILED!"