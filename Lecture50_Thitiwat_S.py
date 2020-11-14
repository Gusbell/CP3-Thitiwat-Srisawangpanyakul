def addNumber(x,y):
    print(x+y)
def minusNumber(x,y):
    print(x-y)
def multipleNumber(x,y):
    print(x*y)
def divideNumber(x,y):
    print(x/y)

while True:
    print("What do you want to do?\n1.add 2.minus 3.multiply 4.divide 5.exit")
    select = int(input("Select: "))
    if select == 1:
        addNumber(int(input("x: ")),int(input("y: ")))
    elif select == 2:
        minusNumber(int(input("x: ")),int(input("y: ")))
    elif select == 3:
        multipleNumber(int(input("x: ")),int(input("y: ")))
    elif select == 4:
        divideNumber(int(input("x: ")),int(input("y: ")))
    elif select == 5:
        break

