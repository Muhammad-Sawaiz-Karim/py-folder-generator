from myFuncs import *
import os

semesterName = getSemester()
subjectList = getClasses()

print("Your current directory is:", os.getcwd())
input("Press enter to generate semester folder in this directory\n")
createSemesterAndClass(semesterName, subjectList)
