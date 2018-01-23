import xml.etree.ElementTree as ET
import sys

tree = ET.parse('worksheet.xml')
root = tree.getroot()
monthTag = ET.SubElement(root, "Month")

def mainMenu():
    print("Select an option")
    print("0) Quit")
    print("1) Check how much your Paycheck will be")
    print("2) Check a goal")
    print("3) Check hours worked")
    menuChoice = input(">")
    return menuChoice

def goalChecker(currentMoney, goal):
    leftToSave = float(goal) - currentMoney
    print("Amount left to save: $" + str(leftToSave))

    hoursToWork = float(leftToSave) / wage
    print("Current hours left to work: " + str(round(hoursToWork)))

def getMonth():
    print("Enter a Month to check its data. (Must be a number!)")
    monthChoice = input(">")
    return int(monthChoice) - 1

def getPaycheckAmount(month):
    totalPay = 0
    for data in root[month].findall('Shift'):
        pay = data.find('Pay').text
        totalPay = totalPay + float(pay)

    #return ("Your total pay for " + root[month][0].text + " will be $" + str(totalPay))
    return totalPay

def calcHoursWorked(month):
    hoursWorked = 0
    for data in root[month].findall('Shift'):
        hours = data.find('Hours').text
        hoursWorked = hoursWorked + float(hours)
    
    return hoursWorked

def addNewShift(getMonth):
    '''jeff'''

wage = float(input("Enter current wage: "))
while True:
    choice = mainMenu()
    if choice == "0" or choice == "q":
        quit()

    if choice == "1":
        month = getMonth()
        print("Your total pay for " + root[month][0].text + " will be $" + str(getPaycheckAmount(month)))

    elif choice == "2":
        curMoney = float(input('Enter the amount you have: '))
        useMonthWage = input("Calculate with monthly wage? (y/n):")
        curGoal = float(input("Enter your goal: "))
        if useMonthWage == 'y':
            month = getMonth()
            monthlyWage = getPaycheckAmount(month)
            factorSavings = input("Factor in savings? (y/n): ")
            if factorSavings == 'y':
                percentCut = int(input("How much savings are you keeping? (percent): "))
                percentCalc = percentCut / 100
                finalMoney = float(curMoney) + (float(monthlyWage) * percentCalc)
            else:
                finalMoney = float(curMoney) + float(monthlyWage)
            goalChecker(finalMoney, curGoal)
        else:
            goalChecker(curMoney, curGoal)

    elif choice == "3":
        month = getMonth()
        print(calcHoursWorked(month))

    elif choice == "4":
        month = getMonth()
        addNewShift(month)
