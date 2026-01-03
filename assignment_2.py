############# create variable,calculate and print it(product name,quantity,price)

product = "book"
quantity = 50
price = 30.0

totalprice = quantity * price
print("product ",product," has total price is ",totalprice)


############ take two number from user and check which number is bigger and,both are equal  

num1 = int(input("enter the firsr number "))
num2 = int(input("enter the second number "))

if num1>num2:
    print(num1 ,"number first is bigger")
elif num1<num2:
    print(num2,"number second is bigger")
else:
    print("both number are equal")

############ take a number from user and check it is +ve,-ve,0

number = int(input("enter a number"))

if number >0:
    print(number ,"is positive")
elif number <0:
    print(number,"is negative")
else:
    print(number,"is zero")

########### take a salary from user if salary >300000 calculate 5% tax and print the remaining salary

salary = float(input("enter your salary"))

if salary > 300000:
    tax = salary*0.05
    print("new salary after paying tax is ", (salary-tax))
else:
    print("salary is ",salary)

############## create varible storing string  and check both string are equal or not

str1 = input("enter the first string")
str2 = input("enter second string")

if str1==str2:
    print("both string are Equal")
else:
    print("both string are not equal")
#print( str1 is str2)

########## take total and obtained marks from user and caculate and print percentage

total_marks = float(input("enter the total marks"))
obtained_marks = float(input("enter the obtained marks"))

percetage = (obtained_marks/total_marks)*100
print("percentage is =",percetage)

########## create variable storing a mobile number .print it's value and data type

mobile_no = 897656789

print(mobile_no)
print(type(mobile_no))

############# take a number from user and check is it divisible by 5 or not 

num= int(input("enter the number"))

if num % 5==0:
    print("divisible by 5")
else:
    print("not divisible by 5")

############ create a variable storing a value  and check whether the value is of type int,float,or string


nam = "oppp"
if type(nam) == int:
    print("type is integer")
elif type(nam) == str:
    print("type of nam is string")
else:
    print("type is float")


#############