import read
from datetime import date, timedelta
slot_date = date(2022, 6, 6)
slot = {}
# slot["1"]=["12/05/2021","1","Zain Iqbal"]
# slot["2"]=["13/05/2021","2","Uzair Iqbal"]

# count students in a course

countCourseStudents = {}

for x in read.courses:
    count = int(0)
    for y in read.studentCourse:
        print(y)
        if y[2]==x[0]:
            count+=1
    countCourseStudents[x[0]]=count

print(countCourseStudents)



