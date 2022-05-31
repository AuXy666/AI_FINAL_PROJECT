import random
import read
from datetime import datetime, timedelta
from copy import deepcopy
import math
import os

# slot["1"]=["12/05/2021","1","Zain Iqbal"]
# slot["2"]=["13/05/2021","2","Uzair Iqbal"]


def randomSlotGenerator(slotsList):
    for x in read.courses:
        #selecting date randomly and checking day should not be sunday and saturday
        while 1:
            randDateIndex = random.randint(0, len(datesForThreeWeeks) - 1)
            day = dayNames[datesForThreeWeeks[randDateIndex].weekday()]
            if day != 'Saturday' and day != 'Sunday':
                break

        # if day != 'Friday':
        #     randTimeIndex = random.randint(0, len(slotsForTwoWeeks) - 1)
        #     slotAssigned = slotsForTwoWeeks[randTimeIndex]
        # else:
        #     slotsFriday = ['9A.M. - 12P.M.', '2P.M. - 5P.M.']
        #     randTimeIndex = random.randint(0, len(slotsFriday) - 1)
        #     slotAssigned = slotsFriday[randTimeIndex]

        randTimeIndex = random.randint(0, len(slotsForThreeWeeks) - 1)
        slotAssigned = slotsForThreeWeeks[randTimeIndex]
        randTeacherIndex = random.randint(0,len(read.teachers)-1)
        totalStudentsForCourse = countCourseStudents[x[0]]
        #Rooms allocation
        roomsAlloted=[]
        while totalStudentsForCourse>0:
            randRoom = random.randint(0, len(read.rooms) - 1)
            if read.rooms[randRoom][0] in roomsAlloted:
                continue
            roomsAlloted.append(read.rooms[randRoom][0])
            totalStudentsForCourse -= 28

        #assigning date, day slot time ,teacher and rooms for a Course exam randomly
        slotsList[x[0]]=[str(datesForThreeWeeks[randDateIndex]),
                     dayNames[datesForThreeWeeks[randDateIndex].weekday()],
                     slotAssigned,
                     read.teachers[randTeacherIndex][0],
                     roomsAlloted]

    return slotsList
def CheckTeacherClash(slotsList):
    teacherChecked = []
    teachersClash = int(0)
    for slot in slotsList:
        teacher = slotsList[slot][3]
        date = slotsList[slot][0]
        if teacher in teacherChecked:
            continue
        teacherChecked.append(teacher)
        for slot1 in slotsList:
            if slot != slot1:
                teacher1 = slotsList[slot1][3]
                date1 = slotsList[slot1][0]
                if teacher == teacher1 and date == date1:
                    print(slot, slot1, teacher, date)
                    teachersClash += 1
        # print(date,end=", ")
    return teachersClash
def CheckRoomClash(slotsList):
    roomChecked = []
    roomClash = int(0)
    for slot in slotsList:
        room = slotsList[slot][4]
        date = slotsList[slot][0]
        time =slotsList[slot][2]
        for r in room:
            if room in roomChecked:
                continue
            roomChecked.append(room)
            for slot1 in slotsList:
                if slot != slot1:
                    room1 = slotsList[slot1][4]
                    date1 = slotsList[slot1][0]
                    time1 = slotsList[slot1][2]
                    if room == room1 and date == date1:
                        if time1 == time:
                             print(slot, slot1, room, date)
                             roomClash += 1
                        elif (time=='1P.M. - 4P.M.'and time1=='2P.M. - 5P.M.') or (time1=='1P.M. - 4P.M.'and time=='2P.M. - 5P.M.'):
                            print(slot, slot1, room, date)
                            roomClash += 1
            # print(date,end=", ")
    return roomClash
def CheckCourseClash(slotsList):
    dateChecked = []
    dateTimeClash = int(0)
    for slot in slotsList:
        time = slotsList[slot][2]
        date = slotsList[slot][0]
        datetime = [date,time]
        if datetime in dateChecked:
            continue
        dateChecked.append(datetime)
        for slot1 in slotsList:
            if slot != slot1:
                time1 = slotsList[slot1][2]
                date1 = slotsList[slot1][0]
                if time == time1 and date == date1:
                    print(slot, slot1,time, time1, date)
                    dateTimeClash += 1
                elif (time=='1P.M. - 4P.M.'and time1=='2P.M. - 5P.M.' and date == date1) or (time1=='1P.M. - 4P.M.'and time=='2P.M. - 5P.M.' and date == date1):
                    print(slot, slot1,time, time1, date)
                    dateTimeClash += 1
        # print(date,end=", ")
    return dateTimeClash
def CheckstudentClash(slotsList):
    print()
    studentCourses = {}
    for stu in read.studentNames:
        temp = []
        for stuCor in read.studentCourse:
            if stu[0] == stuCor[1]:
                temp.append(stuCor[2])
        studentCourses[stu[0]] = temp
    studentclashes = int(0)
    for stu in studentCourses:
        courselist = studentCourses[stu]
        for i in range(0,len(courselist)):
            date1 = slotsList[courselist[i]][0]
            time1= slotsList[courselist[i]][2]
            for j in range(i+1,len(courselist)):
                date2=slotsList[courselist[j]][0]
                time2=slotsList[courselist[j]][2]
                #checking date and time courseList[i] and courseList[j]
                if date1 == date2 and time1 == time2:
                    print(stu,courselist[i],courselist[j])
                    studentclashes+=1
                elif (time2 == '1P.M. - 4P.M.' and time1 == '2P.M. - 5P.M.' and date2 == date1) or (time1 == '1P.M. - 4P.M.' and time2 == '2P.M. - 5P.M.' and date2 == date1):
                    print(stu, courselist[i], courselist[j])
                    studentclashes += 1
    return studentclashes
def solutionCost(slotsList):
    print()
    #checking teacher clashes
    print("\nchecking teachers clash : ")
    totalTeachersClash = CheckTeacherClash(slotsList)
    print("\ntotal teacher clashes = ",totalTeachersClash)
    print("\nchecking rooms clash : ")
    totalRoomClash = CheckRoomClash(slotsList)
    print("\ntotal rooms clashes = ", totalRoomClash)
    print("\nchecking course clash : ")
    totalCourseClash = CheckCourseClash(slotsList)
    print("\ntotal course clashes = ", totalCourseClash)
    print("\nchecking Student clash : ")
    totalStudentClash = CheckstudentClash(slotsList)
    print("\ntotal student clashes = ", totalStudentClash)
    print("total clahes(except course clash) = ",totalStudentClash + totalRoomClash + totalTeachersClash)
    return totalStudentClash + totalRoomClash+ totalTeachersClash
def randomNeighbour(slotList):
    #print(read.courses)
    newSol = deepcopy(slotList)
    randCourseIndex = random.randint(0,len(read.courses)-1)
    code = read.courses[randCourseIndex][0]
    #print(code)
    # selecting date randomly and checking day should not be sunday and saturday
    while 1:
        randDateIndex = random.randint(0, len(datesForThreeWeeks) - 1)
        day = dayNames[datesForThreeWeeks[randDateIndex].weekday()]
        if day != 'Saturday' and day != 'Sunday':
            break

    # if day != 'Friday':
    #     randTimeIndex = random.randint(0, len(slotsForTwoWeeks) - 1)
    #     slotAssigned = slotsForTwoWeeks[randTimeIndex]
    # else:
    #     slotsFriday = ['9A.M. - 12P.M.', '2P.M. - 5P.M.']
    #     randTimeIndex = random.randint(0, len(slotsFriday) - 1)
    #     slotAssigned = slotsFriday[randTimeIndex]

    randTimeIndex = random.randint(0, len(slotsForThreeWeeks) - 1)
    slotAssigned = slotsForThreeWeeks[randTimeIndex]
    randTeacherIndex = random.randint(0, len(read.teachers) - 1)
    totalStudentsForCourse = countCourseStudents[x[0]]
    # Rooms allocation
    roomsAlloted = []
    while totalStudentsForCourse > 0:
        randRoom = random.randint(0, len(read.rooms) - 1)
        if read.rooms[randRoom][0] in roomsAlloted:
            continue
        roomsAlloted.append(read.rooms[randRoom][0])
        totalStudentsForCourse -= 28

    # assigning date, day slot time ,teacher and rooms for a Course exam randomly
    newSol[code] = [str(datesForThreeWeeks[randDateIndex]),
                       dayNames[datesForThreeWeeks[randDateIndex].weekday()],
                       slotAssigned,
                       read.teachers[randTeacherIndex][0],
                       roomsAlloted]
    #print(newSol)
    return newSol
def simulatedAneal(slotList):
    current = slotList
    next = []
    best = current
    temperature = 1000
    coolingRate = 0.2
    while temperature > 1:
        next = randomNeighbour(current)
        E = solutionCost(current) - solutionCost(next)
        if E > 0:
            current = next
            print("Good Move : {}".format(current))
        else:
            probabilty = math.exp(E / temperature)
            current = next
            print("Bad Move : {}\n with probability {}".format(current, probabilty))
        if solutionCost(current) < solutionCost(best):
            best = current
        temperature -= coolingRate
    print("********************************************************************************************\n\nBest solution is :")
    for slot in slotList:
        print(slot, " = ", slotList[slot])
    print("\nsolution cost is :")
    solutionCost(best)


# count students in a course
slots = {}
dayNames=["Monday",'Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
slotsForThreeWeeks=['9A.M. - 12P.M.', '2P.M. - 5P.M.']
datesForThreeWeeks=[]
startDate = datetime(2022, 5, 20)
for i in range(21):
    datesForThreeWeeks.append(startDate.date())
    startDate += timedelta(days=1)
countCourseStudents = {}
for x in read.courses:
    count = int(0)
    for y in read.studentCourse:
        #print(y)
        if y[2] == x[0]:
            count += 1
    countCourseStudents[x[0]] = count
print(countCourseStudents)
print()
slots = randomSlotGenerator(slots)
# slots['CS217'][4] = ['R - 1']
# slots['CS217'][0] = '2022-06-01'
# slots['CS217'][1] = 'Wednesday'
# slots['CS217'][2] = '1P.M. - 4P.M.'
# slots['CS217'][3] = 'Dr. Rabia Maqsood'
# slots['EE227'][4] = ['R - 1']
# slots['EE227'][0] = '2022-06-01'
# slots['EE227'][1] = 'Wednesday'
# slots['EE227'][2] = '2P.M. - 5P.M.'
# slots['EE227'][3] = 'Dr. Rabia Maqsood'
# slots['CS211'][4] = ['R - 1']
# slots['CS211'][0] = '2022-06-01'
# slots['CS211'][1] = 'Wednesday'
# slots['CS211'][2] = '2P.M. - 5P.M.'
# slots['CS211'][3] = 'Dr. Rabia Maqsood'
for slot in slots:
    print(slot, slots[slot])

solutionCost(slots)
os.system("pause")
simulatedAneal(slots)

#n1, n2, n3, n4 = rGen()
#print(n1, n2, n3, n4)





