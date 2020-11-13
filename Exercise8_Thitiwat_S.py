username = input("username: ")
password = input("password: ")
product = ("1.Coconut  20฿", "2.Organic Rice(1kg)  70฿", "3.Dried Mango  35฿")
total = []

if username == "gus" and password == "123":
    print("---Login Success---\nWelcome to GreenBell Shop!!")
    print("Select Menu")
    while True:
        print("1.Product list\n2.Total\n3.Exit")
        x = int(input(">>"))
        if x == 1:
            print(product)
            b = int(input("Select Your Product\n>>"))
            if b == 1:
                print(product[0])
                c = int(input("Quantity: "))
                print("You want to buy Coconut x%d" %c)
                YN = input("Y/N\n")
                if YN == "Y":
                    total.append(c*20)
                else:
                    break
            if b == 2:
                print(product[1])
                d = int(input("Quantity: "))
                print("You want to buy Coconut x%d" %d)
                YN = input("Y/N\n")
                if YN == "Y":
                    total.append(d*20)
                else:
                    break
            if b == 3:
                print(product[2])
                e = int(input("Quantity: "))
                print("You want to buy Coconut x%d" %e)
                YN = input("Y/N\n")
                if YN == "Y":
                    total.append(e*20)
                else:
                    break
        if x == 2:
            f = 0
            for g in total:
                f += g
            print("Total = %d ฿" %f)
            quit = input("Do you want to buy more?\nY/N\n")
            if quit == "Y":
                continue
            else:
                break
        if x == 3:
            print("Do you want to Quit?")
            YN = input("Y/N\n")
            if YN == "Y":
                break
            else:
                continue
            
#จริงๆตรงtotalอยากให้มันแสดงชื่อสินค้าด้วยแต่ พอก่อน :)
