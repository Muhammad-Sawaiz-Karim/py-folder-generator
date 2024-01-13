import os

def getSemester():
    semesterInput = input("Please enter the semester (whitespace will be stripped)\n")
    return semesterInput.replace(" ", "")

def getClasses():
    classString = input("Enter your classes, seperated by commas (whitespace will be stripped)\n")
    strippedString = classString.replace(" ", "")
    return strippedString.split(',')

def createSubfolders():
   subfolderList = ["assignments", "notes", "slides-resources"] #list of subfolders to be created
   for i in subfolderList:
       os.mkdir(i)

def createSemesterAndClass(semesterName, subjectList):
    #creates semester folder and sets working directory to it
    os.mkdir(semesterName)
    os.chdir(semesterName)
    semesterPath = os.getcwd() #used to go back to semester folder after creating one class folder

    for i in subjectList: #creates class folders and subfolders
        os.mkdir(i)
        os.chdir(i)
        createSubfolders()
        os.chdir(semesterPath)

def main():
    semesterName = getSemester()
    subjectList = getClasses()

    print("Your current directory is:", os.getcwd())
    input("Press enter to generate semester folder in this directory\n")
    createSemesterAndClass(semesterName, subjectList)

if __name__ == "__main__":
    main()