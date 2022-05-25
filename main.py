import random

import read
from datetime import date, timedelta
slot_date = date(2022, 6, 6)
slot = {}
# slot["1"]=["12/05/2021","1","Zain Iqbal"]
# slot["2"]=["13/05/2021","2","Uzair Iqbal"]
time = [[9, 12], [2, 5]]

def rGen():
    date_rand = random.range(1, 4)
    room_rand = random.randrange(0, read.rooms)
    teacher_rand = random.randint(0, read.teachers)
    time_rand = random.randint(0, 1)

    print( date_rand, room_rand, teacher_rand, time_rand)

# count students in a course

countCourseStudents = {}

for x in read.courses:
    count = int(0)
    for y in read.studentCourse:
        print(y)
        if y[2] == x[0]:
            count += 1
    countCourseStudents[x[0]] = count

print(countCourseStudents)
print()
rGen()
#n1, n2, n3, n4 = rGen()
#print(n1, n2, n3, n4)





