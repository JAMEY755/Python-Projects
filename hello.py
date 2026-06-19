print("Student Details")
student_name="Jamey"
student_id=1234
gpa=4.3
is_registerd=True

print("NAME:", student_name, )
print("ID:", student_id, )
print("GPA:", gpa, )
print("REGISTRATION STATUS:", is_registerd)

print("NAME:", student_name, type(student_name))
print("ID:", student_id, type(student_id))
print("GPA:", gpa, type(gpa))
print("REGISTRATION STATUS:", is_registerd, type(is_registerd))

# Age calculator
birth_year=int(input("Enter your birth year "))
current_year=2026
age =current_year-birth_year
print(f"You are {age} years old")