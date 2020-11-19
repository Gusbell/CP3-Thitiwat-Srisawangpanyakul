class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added to " +self.name+ " " + self.lastName + "'s cart")

customer1 = Customer()              
customer1.name = "Bob"
customer1.lastName = "Baby"
customer1.age = 8
customer1.addCart()

customer2 = Customer()              
customer2.name = "Rias"
customer2.lastName = "Graymory"
customer2.age = 17
customer2.addCart()

customer3 = Customer()              
customer3.name = "Twilight"
customer3.lastName = "Healing"
customer3.age = 14 
customer3.addCart()

customer4 = Customer()              
customer4.name = "Nekomata"
customer4.lastName = "Koneko"
customer4.age = 16 
customer4.addCart()

customer5 = Customer()              
customer5.name = "ขี่ม้าคนวงทวน"
customer5.lastName = "ฝนหนาวสาวคราง"
customer5.age = 20
customer5.addCart()
