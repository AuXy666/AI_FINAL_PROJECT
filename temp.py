import random
import read

hello = "  =  "
studentCourses = {}
for stu in read.studentNames:
    temp = []
    for stuCor in read.studentCourse:
      if stu[0] == stuCor[1]:
            temp.append(stuCor[2])
    studentCourses[stu[0]] = temp
for x in studentCourses:
    print(f"{x:>50}{hello}{studentCourses[x]}")