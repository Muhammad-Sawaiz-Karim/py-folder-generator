import os

def getPath():
    while True:
        directoryInput = input("Enter the path of the folder where you want to create the folder.\nType 'n' to create the folder here.\n")

        if (os.path.exists(directoryInput)):
            os.chdir(directoryInput)
            break
        elif (directoryInput == "n"):
            print(os.getcwd())
            break
        else:
            print("Path does not exist, please try again")

def getSemester():
    semesterInput = input("Please enter the semester (whitespace will be stripped)\n")
    return semesterInput.replace(" ", "") #didn't use .strip() because it only removed first and last whitespace

def getClasses():
    classString = input("Enter your classes, seperated by commas (whitespace will be stripped)\n")
    strippedString = classString.replace(" ", "")
    return strippedString.split(',') #didn't use .strip() because it only removed first and last whitespace

def createSubfolders():
   subfolderList = ["assignments", "notes", "slides-resources"] #list of subfolders to be created
   for i in subfolderList:
       if (not os.path.exists(i)):
           os.mkdir(i)

def createSemesterAndClass(semesterName, subjectList):
    #creates semester folder and sets working directory to it

    os.mkdir(semesterName)
    os.chdir(semesterName)
    semesterPath = os.getcwd() #used to go back to semester folder after creating one class folder

    for i in subjectList: #creates class folders and subfolders
        if (not os.path.exists(i)):
            os.mkdir(i)
        os.chdir(i)
        createSubfolders()
        os.chdir(semesterPath)
        
