import time


def reading(csvFile):
    with open(csvFile, "r") as txt:
        students = []
        bool = True
        while bool == True:
            student = txt.readline()
            if student == '':
                bool = False
            else:
                student = student.strip("\n")
                student = student.split(",")
                student = student[0:4]
                students.append(student)
        return students
        txt.close()


start = time.perf_counter()
Alist = reading("Banner Email Validate.csv")
Blist = reading("Inspire Active Students 01-24-22.csv")
duplicates = []
nonExistA = []
nonExistB = []
cycleA = 33244
cycleB = 33342

for i in range(cycleB):
    if i != 0:
        for j in range(cycleA):
            if j == 0:
                continue
            elif Blist[i][2] == Alist[j][2]:
                if Alist[j][3] != Blist[i][3]:
                    duplicates.append(Alist[j])
                    duplicates.append(Blist[i])
                break
            else:
                if j == cycleA - 1:
                    nonExistB.append(Blist[i])

for i in range(cycleA):
    if i != 0:
        for j in range(cycleB):
            if Alist[i][2] == Blist[j][2]:
                break
            elif j == cycleB - 1:
                nonExistA.append(Alist[i])


with open("different_emails.csv", "w") as txt:
    txt.write("Banner Record\nInspire Record\n")
    for i in range(len(duplicates)):
        txt.write(f"{duplicates[i][0]},{duplicates[i][1]},{duplicates[i][2]},{duplicates[i][3]}")
        txt.write("\n")
    txt.close()

with open("NotContainedInBanner.csv", "w") as txt:
    txt.write(f"{len(nonExistB)} records not found in Banner Data\n")
    for i in range(len(nonExistB)):
        txt.write(f"{nonExistB[i][0]},{nonExistB[i][1]},{nonExistB[i][2]},{nonExistB[i][3]}")
        txt.write("\n")
    txt.close()

with open("NotContainedInInspire.csv", "w") as txt:
    txt.write(f"{len(nonExistA)} records not found in Inspire Data\n")
    for i in range(len(nonExistA)):
        txt.write(f"{nonExistA[i][0]},{nonExistA[i][1]},{nonExistA[i][2]},{nonExistA[i][3]}")
        txt.write("\n")
    txt.close()


stop = time.perf_counter()
print(stop-start)


