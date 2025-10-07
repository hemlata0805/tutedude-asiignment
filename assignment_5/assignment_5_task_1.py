student={"hemlata":85,"Arha":95}
student_name=input("Enter the student's name: ")
student_marks=input("{}'s marks:".format(student_name))
student[student_name] = student_marks
print(student)

find_student=input("Enter the student's name: ")
if find_student in student:
    print("{}'s marks are: {}".format(find_student,student[find_student]))
else:
    print("Student not found")