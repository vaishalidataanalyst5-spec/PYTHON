######## 11111111111

class student:
    pass


ram =student()
print(ram)
shyam =student()
print(shyam)
hari =student()
print(hari)

######## 2222

class student:
    pass


ram =student()
ram.id = 1
ram.name = "Ram"
ram.marks = 90

print("id   :",ram.id)
print("name :",ram.name)
print("marks:",ram.marks)
print("--------------------------------")
shyam =student()
shyam.id = 2
shyam.name = "Shyam"
shyam.marks = 89.0
print("id   :",shyam.id)
print("name :",shyam.name)
print("marks:",shyam.marks)
print("-----------------------------------")
hari =student()
hari.id= 3
hari.name ="Hari"
hari.marks = 78.9
print("id   :",hari.id)
print("name :",hari.name)
print("marks:",hari.marks)

# it takes lengthy code and so below is the best way to write class ,object and it's state and behavior



class employee:
    def set(self,id,name,salary):#local variable
        self.id = id
        self.name = name
        self.salary = salary
    def show(self):
        print("id is   :",self.id)
        print("name is :",self.name)
        print("salary is :",self.salary)


    

vaishali = employee()
vaishali.set(1001,"Vaishali",500000)
vaishali.show()
print("-----------------------------")
prashant = employee()
prashant.set(1011,"Prashant",100000000)
prashant.show()
