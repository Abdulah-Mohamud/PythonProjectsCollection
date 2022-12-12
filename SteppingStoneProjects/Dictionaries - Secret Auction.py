student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

final_grade = ""
for grade in student_scores:
    if student_scores[grade] >= 91 and student_scores[grade] <= 100:
        final_grade = "Outstanding"
    elif student_scores[grade] >= 81:
        final_grade = "Exceed Expectation"
    elif student_scores[grade] >71:
        final_grade = "Acceptable"
    else:
        final_grade = "Fail"

    student_grades[grade] = final_grade

print(student_grades)
