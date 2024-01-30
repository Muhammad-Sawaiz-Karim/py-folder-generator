from myFuncs import * #importing functions
import os

semesterName = getSemester()
subjectList = getClasses()
getPath()

print("Your current directory is:", os.getcwd())
input("Press enter to generate semester folder in this directory\n")
createSemesterAndClass(semesterName, subjectList)
