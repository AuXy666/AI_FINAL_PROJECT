import read

slot = {}
# slot["1"]=["12/05/2021","1","Zain Iqbal"]
# slot["2"]=["13/05/2021","2","Uzair Iqbal"]

totalSlots = range(30)
j = 0
k = 0
for i in totalSlots:
    if i == 15:
        j = 0
    if i == 10 or i == 20:
        k = 0
    temp = str(read.courses[j][0])
    slot[temp] = ["12/05/2021", read.rooms[k][0], read.teachers[i][0]]
    #slot[]
    j = j+1
    k = k+1

print(slot)

