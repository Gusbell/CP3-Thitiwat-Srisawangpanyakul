menuList = []

def showBill():
    print("---- My Food ----")
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])

def showTotal():
    total = 0
    print("---- Total ----")
    for number in menuList:
        total += int(number[1])
    print("Total is %d Bath" %total)

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append([menuName,menuPrice])
showBill()
showTotal()
