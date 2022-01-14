#Grade Calculator

#The final grade should be calculated using the following weights:
#Assignments -% Midterm -% Tutorials -% Final Exam -%
#To pass the course, the student must have a final grade of 60% or higher
#and have received at least 50% on the final exam.


#Get weights
assignment_weight = int (input("What is the assignment weight? "))
midterm_weight = int (input("What is the midterm weight? "))
tutorial_weight = int (input("What is the tutorial weight? "))
final_weight = int (input ("What is the final weight? "))

#Get marks
assignment_mark = float (input("What is the assignment mark? "))
midterm_mark = float (input("What is the midterm mark? "))
tutorial_mark = float (input("What is the tutorial mark? "))
final_mark = float (input ("What is the final mark? "))

#calculate Grade
grade = ((assignment_weight/100) * assignment_mark + (midterm_weight/100) * midterm_mark + (tutorial_weight/100) * tutorial_mark + (final_weight/100) * final_mark)

#print(f"grade: {grade}%")

if final_mark >= 50 and grade >= 50:
    print("you pass")
    print(f"grade: {grade}%")
else:
    print("you fail")
    print(f"grade: {grade}%")
