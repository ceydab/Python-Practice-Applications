'''this project creates an algorithm to calculate final grade. the algorithm starts with a function to obtain the grades from .txt file.
each line (representing each student) is passed through calculateGrade() function that calculates the average grade and letter grade
for each student. entergrade() function allows the user to enter these grades into .txt file, savegrade allows saving the freshly entered
grades. finally a while loops asks the user what s/he wants to do, and chooses the action (function) to take.
'''
def getAverage():
    with open("exam_grades.txt", "r") as file:
        for line in file:
            print(calculateGrade(line))

def calculateGrade(line):
    line = line[:-1]
    listit = line.split(":")
    names = listit[0]
    sepgrades = listit[1]
    listgrades = sepgrades.split(",")
    average = (int(listgrades[0]) + int(listgrades[1]) + int(listgrades[2]))/3
    #print("\n", names , average)
    if average > 90:
        letter = "AA"
    elif average >=85 and average <= 89:
        letter = "BA"
    elif average >=80 and average <= 84:
        letter = "BB"
    elif average >=75 and average <= 79:
        letter = "CB"
    elif average >=70 and average <= 74:
        letter = "CC"
    elif average >=65 and average <= 69:
        letter = "DC"
    elif average >=60 and average <= 64:
        letter = "DD"
    elif average >=50 and average <= 59:
        letter = "FD"
    elif average <= 49:
        letter = "FF"
    return "\n" + names + ": " + str(average) + "\nLetter grade: " + letter


def enterGrades():
    name = input("Student name: ")
    grade1 = input("Grade 1 = ")
    grade2 = input("Grade 2 = ")
    grade3 = input("Grade 3 = ")

    with open("exam_grades.txt", "a") as file:
        file.write(name + ": " + grade1 + " , " + grade2 + " , " + grade3 + "\n")
        


def saveGrades():
    with open("exam_grades.txt", "r") as file:
        listit2 = []
        
        for i in file:
            listit2.append(calculateGrade(i))
    
        with open("results.txt", "w") as file2:
            for i in listit2:
                file2.write(i)

while True:
    ask = input("1- Read the grades \n2- Enter new grades \n3- Save the grades \n4- Exit\n")
    if ask == '1':
        getAverage()
    elif ask == '2':
        enterGrades()
    elif ask == '3':
        saveGrades()
    else:
        break
