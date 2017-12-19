import random
import time
import os

Money = 10000
BTCStartPrice = 9000
HeldStockAmount = 1
MoneySpent = 0
MoneyGained = 0

with open("savedata") as savedataread:
    for i, line in enumerate(savedataread):
        if i == 0:
            Money = int(line.strip())
        if i == 1:
            HeldStockAmount = int(line.strip())



def openMarketTrade(BTCStartPrice):
	openingUD = random.uniform(0.01, 0.5)
	choice = ['up', 'down']
	UDchoice = random.choice(choice)
	if UDchoice == "up":
		finalOpenPrice = round(BTCStartPrice / openingUD)
		return finalOpenPrice
	elif UDchoice == "down":
	    finalOpenPrice = round(BTCStartPrice * openingUD)
	    return finalOpenPrice
BTCPrice = openMarketTrade(BTCStartPrice)



def selectBuy(MoneyAmount, BTCPrice, LHeldStockAmount):
        PurchaseStockAmount = input("How many stocks would you like to buy? ")
        StockBuyCost = int(BTCPrice) * int(PurchaseStockAmount)
        print("You will be buying " + str(PurchaseStockAmount) +  " stocks at the price of $" + str(StockBuyCost) + ".")
        time.sleep(2)
        if StockBuyCost > MoneyAmount:
            print("Sorry, You don't have enough for that.")
        else:
            global Money
            global HeldStockAmount
            global MoneySpent
            Money = MoneyAmount - StockBuyCost
            HeldStockAmount = int(LHeldStockAmount) + int(PurchaseStockAmount)
            MoneySpent = MoneySpent + StockBuyCost
            print("Success! You now own " + str(HeldStockAmount) + " shares, and you have $" + str(Money) + " left." )
            time.sleep(3)

def selectSell(MoneyAmount, BTCPrice, LHeldStock):
    SellStockAmount = input("How many stocks do you want to sell? ")
    StockSellCost = int(BTCPrice) * int(SellStockAmount)
    print("You will be selling " + str(SellStockAmount) + " stocks at the price of $" + str(StockSellCost) + ".")
    time.sleep(2)
    if int(SellStockAmount) > LHeldStock:
        print("Sorry, you don't have that many stocks.")
    else:
        global Money
        global HeldStockAmount
        global MoneyGained
        Money = MoneyAmount + StockSellCost
        HeldStockAmount = int(LHeldStock) - int(SellStockAmount)
        MoneyGained = MoneyGained + StockSellCost
        print("Success! You sold " + str(SellStockAmount) + " stocks and earned a total of $" + str(StockSellCost))
        time.sleep(3)


def MainMenu():
        print ("The current price of BTC is: $" + str(BTCPrice))
        print ("Your current funds are: $" + str(Money))
        print ("You currently hold " + str(HeldStockAmount) + " stock(s).")
        menuInput = input("What will you do? (B)uy, (S)ell or (E)xit: ")
        return menuInput

def MenuChoice(menuInput):
        if menuInput == "B":
            selectBuy(Money, BTCPrice, HeldStockAmount)
        elif menuInput == "S":
            selectSell(Money, BTCPrice, HeldStockAmount)
        elif menuInput == "E":
            print("See you later!")
            print("You spent a total of $" + str(MoneySpent))
            print("You earned a total of $" + str(MoneyGained))

            WriteSaveData(Money, HeldStockAmount)

            global isRunning
            isRunning = False

        else:
            print("Incorrect input entered. Please try again.")
            time.sleep(2)

def StockRandomizer(BTCStartPrice):
    UD = random.uniform(0.01, 1)
    choice = ['up', 'down']
    UDchoice = random.choice(choice)
    if UDchoice == "up":
        finalPrice = round(BTCStartPrice / UD)
        global BTCPrice
        BTCPrice = finalPrice
        return finalPrice
    elif UDchoice == "down":
        finalPrice = round(BTCStartPrice * UD)
        BTCPrice = finalPrice
        return finalPrice

def WriteSaveData(MoneyAmount, HeldStockAmount):
    openFile = open("savedata","w")
    openFile.truncate()
    openFile.write(str(MoneyAmount) + '\n')
    openFile.write(str(HeldStockAmount))
    openFile.close()

global isRunning
isRunning = True
def runProgram():
    while isRunning == True:
            MenuChoice(MainMenu())
            StockRandomizer(BTCStartPrice)


runProgram()
