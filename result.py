
# question 1

students = []

for i in range(5):

    name = input("Enter your name: ")
    print("Name = ", name)

    roll_number = int(input("Enter your roll number: "))
    print("Roll_Number = ", roll_number)

    print("Marks of 3 subjects.")

    python_marks = int(input("Enter your python marks "))
    artifical_intelligence = int(input("Enter your AI marks "))
    mathematics = int(input("Enter your MATHS marks "))

    total_marks = python_marks + artifical_intelligence + mathematics
    percentage = total_marks / 3

    if percentage >= 80:
        Grade = "A"
    elif percentage >= 70:
        Grade = "B"
    elif percentage >= 60:
        Grade = "C"
    elif percentage >= 50:
        Grade = "D"
    else:
        Grade = "Fail"

    student = {
        "Name": name,
        "Roll number": roll_number,
        "Total_marks": total_marks,
        "Percentage": percentage,
        "Grade": Grade
    }

    students.append(student)


print("<========Student results===========>")

for student in students:
    print("Name =", student["Name"])
    print("Roll number =", student["Roll number"])
    print("Total_marks =", student["Total_marks"])
    print("Percentage =", student["Percentage"])
    print("Grade =", student["Grade"])


highest = students[0]

for student in students:
    if student["Percentage"] > highest["Percentage"]:
        highest = student

print("Name =", highest["Name"])
print("Percentage =", highest["Percentage"])


file = open("result.txt", "w")

for student in students:
    file.write("Name = " + student["Name"] + "\n")
    file.write("Roll Number = " + str(student["Roll number"]) + "\n")
    file.write("Total = " + str(student["Total_marks"]) + "\n")
    file.write("Percentage = " + str(student["Percentage"]) + "\n")
    file.write("Grade = " + student["Grade"] + "\n")
    file.write("\n")

file.close()

