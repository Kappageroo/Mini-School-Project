import csv
import math

#FUNCTIONS#
def gradecheck (inputname):
    found = False
    with open(r"c:\code2\school_roster_grades.csv", mode="r") as sg:
        csvread = csv.DictReader(sg)
        for row in csvread:
            name = row["name"]
            try:    
                grade = float(row["grade"])
            except ValueError:
                continue
            if inputname.lower().strip() == name.lower().strip():
                print(f"{row['name']} your grade is {row['grade']}")
                found = True
                break
    if found is not True:
        print("Your name is not found!")
        print("Please contact your teacher.")

def absencecheck(inputname): #Passing, Needs Improvement, At Risk, Excellent
    found = False
    with open(r"c:\code2\school_roster_grades.csv", mode="r") as sg:
        csvread = csv.DictReader(sg)
        for row in csvread:
            name = row["name"]
            absence = row["absences"]
            status = row["status"]
            if inputname.lower().strip() == name.lower().strip():
                print("-----------RESULT-----------")
                print(f"Number of absence: {absence}")
                print(f"Status : {status}")
                print("----------------------------")
                found = True
                break
    if found is not True:
        print("Your name is not found!")
        print("Please contact your teacher.")  

def underscorecheck (filepath, mingr): #c:\code2\grades.csv
    totalst = 0
    totalgr = 0
    avergr = 0
    nosuc = 0
    fails = []
    with open(filepath, mode="r") as sg:
        csvread = csv.DictReader(sg)
        print("*----------SCANNING----------*")
        print("Underscored Students:")
        for row in csvread:
            name = row["name"]
            try:    
                grade = float(row["grade"])
            except ValueError:
                continue
            totalst += 1
            totalgr += grade
            if grade < mingr:
                nosuc += 1
                print(f"{row['name']:10} = {row['grade']}")
                fails.append({"name": row["name"], "grade": row["grade"], "status": "Underscored"})
        if nosuc == 0:
            print("There's No Underscored Students in Class!")
    avergr = round(totalgr / totalst)
    print("----------SCAN COMPLETE----------")
    print(f"Number of students: {totalst}")
    print(f"Average grades: {avergr}")
    print(f"number of underscored students: {nosuc}")
    print("---------------------------------")
    with open (r"c:\code2\remediation_report.csv", mode="w", newline="") as rr:
        field_names = ["name", "grade", "status"]
        writer = csv.DictWriter(rr, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(fails)

print("----------------------------------------")
print("Welcome To School Web 1.0".center(41))
print("----------------------------------------")
print("Are you a student (S) or a teacher? (T):")
opt = ("T", "S")
running = True
login_opt = input().upper()
while running:
    while login_opt not in opt:
            print("Not a valid option, please try again.")
            login_opt = input().upper()
            
    if login_opt == "T":
        tstatus = True
        while tstatus:
            print("What would you like to do?")
            print("1. Scan for remidials")
            print("Press Q to Quit")
            avaliable_opt = ("1", "Q")
            topt = input("Option: ").upper().strip()
            while topt not in avaliable_opt:
               print("Please try again.")
               topt = input("Option: ").upper().strip()
               if topt == "1":
                filepath = input("Please enter file path : ")
                pg = int(input("Please enter passing grade : "))
                underscorecheck(filepath, pg)
               elif topt == "Q":
                   running = False
                   tstatus = False

    elif login_opt == "S":
        sstatus = True
        while sstatus:
            print("What would you like to do?")
            print("1. Check Your Grades")
            print("2. Check Your Absence")
            print("3. Check The Semester Schedule ")
            print("Press Q to Quit")
            avaliable_opt = ("1", "2", "3", "Q")
            sopt = input("Option : ").upper().strip()
            while sopt not in avaliable_opt:
                print("Please try again.")
                sopt = input("Option : ").upper().strip()
            if sopt == "1":
                inputname = input("Please enter your name: ").lower().strip()
                gradecheck(inputname)
            elif sopt == "2":
                inputname = input("Please enter your name: ").lower().strip()
                absencecheck(inputname)
            elif sopt == "Q":
                running = False
                sstatus = False