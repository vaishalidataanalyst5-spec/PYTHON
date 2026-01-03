
# book example, is,name,price and auther


class book:
    def getbook(self,id,name,price,auther):
        self.id =id
        self.name = name
        self.price = price
        self.auther = auther
    def showbook(self):
        print("book id is     :",self.id)
        print("book name is   :",self.name)
        print("book price is  :",self.price)
        print("book auther is :",self.auther)
        





b1 = book()
b1.getbook(1,"Urmilla",500,"Samar")
b1.showbook()

print("-----------------------------")

b2 = book()
b2.getbook(2,"YAYYATI",890,"abc")
b2.showbook()

print("--------------------------------")

b3 = book()
b3.getbook(3,"Radhey",450,"rty")
b3.showbook()

print("--------------------------------")

b4 =book()
b4.getbook(4,"MAHABHARAT",2000,"uyt")
b4.showbook()

print("-----------------------------------")

b5 =book()
b5.getbook(5,"RAMAYAN",1000,"Walmiki")
b5.showbook()


#product example  id,name,quantity,unitprice,category


class product:
    def selectProduct(self,id,pname,quantity,unitprice,category):
        self.id =id
        self.pname =pname
        self.quantity =quantity
        self.unitprice=unitprice
        self.category = category
    def getTotalPrice(self):
        self.totalPrice = self.quantity * self.unitprice
    def showBill(self):
        print("-----------Bill Details----------")
        print("product id   :",self.id)
        print("product name  :",self.pname)
        print("quantity :",self.quantity)
        print("unitprice is :",self.unitprice)
        print("category is :",self.category)
        print("total price is :", self.totalPrice)
        print("Thank You..........Visit Again........")

        

    
p1 = product()
p1.selectProduct(1,"Laptop",5,30000,"Electronics")
p1.getTotalPrice()
p1.showBill()


p2 = product()
p2.selectProduct(2,"TV",1,50000,"Electronics")
p2.getTotalPrice()
p2.showBill()


p3 = product()
p3.selectProduct(3,"Saree",3,500,"Clothing")
p3.getTotalPrice()
p3.showBill()

p4 = product()
p4.selectProduct(4,"Bangles",2,100000,"Gold_jwellary")
p4.getTotalPrice()
p4.showBill()

p5 = product()
p5.selectProduct(5,"Sunscreen",10,400,"Beauty_product")
p5.getTotalPrice()
p5.showBill()



#user example username,password,email,mobno,age,address


class user():
    def getUserDetails(self,username,password,gmail,age,mobno = 9876567854,address ="Baner Pune"):
        self.username = username
        self.password = password
        self.gmail = gmail
        self.age = age
        self.mobno = mobno
        self.address = address
   
        
    def showUserDetails(self):
        print("--------logged in successfully----------")
        print("Name   :",self.username )
        print("Gamil  :",self.gmail)
        print("Age    :",self.age)
        print("MobNo  :",self.mobno)
        print("Address:",self.address)

    def islogin(self,username,password):
         if self.username == username and self.password == password:
             self.showUserDetails()
         else:
             print("Login Failed...... \nplease check username and password once")




        


u1 = user()
u1.getUserDetails("vaishali","123","abc@gamil.com",23,9087654334,"Pune")
u1.islogin("vaishali","123")

print("--------------------------------------------")


u2 =user()
u2.getUserDetails("Prashant","456","huy@gmail.com",30)
u2.islogin("Prashant","456")

print("--------------------------------------------")

u3 =user()
u3.getUserDetails("Aadi","1111","hgi@gmail.com",40,"Dharashiv")
u3.islogin("sghjh","1111")

print("--------------------------------------------")

u4 = user()
u4.getUserDetails("Raj","777","ttr@gamil.com",35,9865347356,"Lonavala")
u4.islogin("Raj","777")

print("--------------------------------------------")

u5 = user()
u5.getUserDetails("Suvarna","8899","gghh@gmai.com",25,"Barshi")
u5.islogin("suvarna","098")
