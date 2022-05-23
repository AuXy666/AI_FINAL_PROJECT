import pandas

# reading test_courses.csv

x_courses = pandas.read_csv("test_dataset/test_courses.csv", header=None)
print("Course Id and Course Names")
print(x_courses)

print("\n\n\n")
courses = [list(row) for row in x_courses.values]

# reading test_rooms.csv

x_rooms = pandas.read_csv("test_dataset/test_rooms.csv", header=None)
print("Room Name and Capacity")
print(x_rooms)

print("\n\n\n")
rooms = [list(row) for row in x_rooms.values]

# reading test_studentCourse
# course[0][0] == studentCourse[0][2]

x_studentCourse = pandas.read_csv("test_dataset/test_studentCourse.csv", header=1)
print("ID , StudentName , Course Code")
print(x_studentCourse)

print("\n\n\n")
studentCourse = [list(row) for row in x_studentCourse.values]


# reading test_studentNames
# studentNames[0][0] == studentCourse[0][1]

x_studentNames = pandas.read_csv("test_dataset/test_studentNames.csv", header=0)
print("StudentName")
print(x_studentNames)

print("\n\n\n")
studentNames = [list(row) for row in x_studentNames.values]


# reading test_teachers

x_teachers = pandas.read_csv("test_dataset/test_teachers.csv", header=0)
print("TeacherName")
print(x_teachers)

print("\n\n\n")
teachers = [list(row) for row in x_teachers.values]

