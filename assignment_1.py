############ Print the variable and it's type

name ='vaishali'
age = 30
height = 5.3

print("name is :",name,"\n type of name is ",type(name))
print("age is :",age,"\n type of age is ",type(age))
print("height is :",height,"\n type of height is ",type(height))


#################################### perform arithmetic operation

num1 = int(input("enter the first number :"))
num2 = int(input("enter the second number :"))
print(f"Addition is :{num1+num2} \n Substraction is : {num1-num2} \n Multiplication is : {num1*num2} \n Division is :{num1/num2} \n Floor Division is :{num1//num2} \n Modulus is :{num1%num2}")
      
################################### Even odd Number

num = int(input("enter the number :"))

if num % 2 ==0:
    print(num," is even number")
else:
    print(num," is odd number")

################# take marks of student and check whethe he/she is pass or fail

marks = float(input("enter the marks :"))

if marks >= 40:
    print("student is pass with marks", marks)
else:
    print("student is failed with marks",40-marks)

######## create variables and check equal,not eqaul,greater

no1 = int(input("enter the first number :"))
no2 = int(input("enter the second number :"))
if no1 > no2:
    print(no1,no2 ,"are not equal and",no1 ," first number is greater")
elif no1 == no2:
    print("both number are equal")
else:
    print(no2," second number  is grater")

########### take a number from user and check >10 and <50 ( use logical operator)

num = int(input("Enter the number :"))
if num>10 and num<=50:
    print(num," is in between 10 to 50")
else:
    print(num," is not in between 10 to 50 ")

##############333333 take a bill amount if billamount > 2000 apply 10% discount and print it

bill_amt = float(input("Enter the bill amount :"))
if bill_amt >= 2000:
    discount = bill_amt*0.1
    bill_amt -= discount
   # print("final bill amount is :",bill_amt)
print("final bill amount",bill_amt)

############## check eligible for voting or not

age = int(input("Enter your Age: "))
if age >=18:
    print("Eligible for voting")
else:
    print("not eligible for voting")

############# check specific charachter present in string (use membership operator)

eassy ="hellow world,loved to learn python,python is really interesting"
print("to" in eassy)

############ create variable and demonstrate difference between "==" and "is"


a= 10
b= 10

print(a==b)
print( a is b)