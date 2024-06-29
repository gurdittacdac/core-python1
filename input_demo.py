student_name = input("Enter student name : ")
student_age = input("Enter student age : ")

print("the name of student is {0} and age is {1}".format(student_name,student_age))

print("student Name type",type(student_name))
print("student age type",type(student_age))
"""
if you want to change the type to integer
then we have to add int before input
"""
student_age = int(input("Enter student age : ")) 
print("student age type",type(student_age))


#Example
if student_age >=18:
    print("student is eligible for vote in 2024")
else:
    print("student is not eligible for vote in 2024")
if student_name == "Gurditta":
    print("student name is Gurditta")
if student_name == "Pooja":
    print("student name is Pooja")
if student_name == "Gagandeep":
    print("student name is Gagandeep")
else:
    print("Mention valid name")

if student_age >=18:
    print(f" Final name is {student_name} you are are lucky to get admission in one of the best cources of ACTS")
    print("Pass")
    #we only need to add f only once then and we can add as many format specifier as we can
    print(f" Final name is {student_name} you are are lucky to get admission in "student_age" one of the best cources of ACTS")
else:
    print("you are not eligible for this course")



