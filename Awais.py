import random
from datetime import datetime,timedelta
import read


def randomSlotGenerator():
    for x in read.courses:
        randDateIndex = random.randint(0,len(datesForTwoWeeks)-1)
        randTimeIndex = random.randint(0,len(slotsForTwoWeeks)-1)
        randTeacherIndex = random.randint(0,len(read.teachers)-1)
        totalStudentsForCourse = countCourseStudents[x[0]]
        roomsAlloted=[]
        while totalStudentsForCourse>0:
            randRoom = random.randint(0, len(read.rooms) - 1)
            roomsAlloted.append(read.rooms[randRoom][0])
            totalStudentsForCourse -= 28

        slots[x[0]]=[str(datesForTwoWeeks[randDateIndex]),
                     dayNames[datesForTwoWeeks[randDateIndex].weekday()],
                     slotsForTwoWeeks[randTimeIndex],
                     read.teachers[randTeacherIndex][0],
                     roomsAlloted]

    for slot in slots:
        print(slot,slots[slot])

slots = {}
dayNames=["Monday",'Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
slotsForTwoWeeks=['9A.M. - 12P.M.','1P.M. - 4P.M.','2P.M. - 5P.M.']
datesForTwoWeeks=[]
startDate = datetime(2022, 5, 20)
for i in range(14):
    datesForTwoWeeks.append(startDate.date())
    startDate += timedelta(days=1)
#print(datesForTwoWeeks)
#rand = random.randint(0,len(datesForTwoWeeks)-1)
#print(datesForTwoWeeks[rand],dayNames[datesForTwoWeeks[rand].weekday()])
countCourseStudents = {}
for x in read.courses:
    count = int(0)
    for y in read.studentCourse:
        print(y)
        if y[2] == x[0]:
            count += 1
    countCourseStudents[x[0]] = count
print(countCourseStudents)
#print(read.rooms)

randomSlotGenerator()
