menuList = []
priceList = []

def showBill():
    print("---- My Food ----")
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])

def showTotal():
    total = 0
    print("---- Total ----")
    for number in priceList:
        total += int(number)
    print("Total is %d Baht" %total)

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()
showTotal()
