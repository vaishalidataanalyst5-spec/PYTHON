# Constructor Example


class Product:
    def __init__(self,id,name,category,price):
        self.id = id
        self.name =name
        self.category= category
        self.price = price

    def showProduct(self):
        print(f"Product id :",self.id)
        print(f"Product name :",self.name)
        print(f"Product category :",self.category)
        print(f"Product price :",self.price)

    
p1 =Product(1,"TV","Elctronics",30000)
p1.showProduct()
print("\n")
p2 = Product(2,"mobile","Elctronics",50000)
p2.showProduct()


#### 2


class Book:
    def __init__(self,name,author,price):
       
        self.name =name
        self.author= author
        self.price = price

    def showBook(self):
        
        print(f"bool name :",self.name)
        print(f"book category :",self.author)
        print(f"book price :",self.price)

    
b1 =Book("Urmilla","Samar",300)
b1.showBook()
print("\n")
b2 = Book("Radhey","Priya",500)
b2.showBook()



############ 3


class User:
    def __init__(self,username, password,mobile_no):
        self.username = username
        self.password = password
        self.mobile_no = mobile_no

    def display(self):
        print(f"username is : {self.username}")
        print(f"User password is : {self.password}")
        print(f"mobile no is : {self.mobile_no}")


u1 = User("Adi",1234,6754345678)
u1.display()

print("\n")

u2 = User("Vikas",4567,9876567890)
u2.display()

