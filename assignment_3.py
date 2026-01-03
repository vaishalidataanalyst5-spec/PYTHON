#######1 print numbers from 1 to 10 using for loop

for i in range(1,11):
    print(i)


#####2 print numbers from 1 to 50 and check whether each number is even or odd

for i in range(1,51):
    if i%2==0:
        print(i,"Even Number")
    else:
        print(i,"Odd Number")

####3 print numbers from 1 to 100  and print only those numbers that are divisible by 3

for i in range(1,101):
    if i%3 ==0:
        print(i)

###4 print numbers from 1 to 100 and print "Fizz" if divisible by 3,"Buzz" if divisible by 5,and "FizzBuzz" if divisible by both(use if-elif-else)


for i in range(1,101):
    if i%3 ==0 and i%5==0:
        print(i,"FizzBizz")
    elif i%5 ==0:
        print(i,"Bizz")
    elif i%3 ==0:
        print(i,"Fizz")
    else:
        print(i,"not divisible by 3,5 or 3,and 5")


####5 take a number from the user and print its multiplication table from 1 to 10

number = int(input("enter the number "))

for i in range(1,11):
    print(number, "*", i ," = ",number*i)


####6 take a number from the user and calculate the sum of digits using a for loop

number = input("enter the number ")
sum=0
for i in range(len(number)):
    sum+= int(number[i])
print("sum of digits is :",sum)


###7 take a number from the user and count how many digits it has

number = input("enter the number")
print("the number has ",len(number),"digits")


####8 take a number from the user and calculate its factorial using a for loop

number = int(input("enter the number "))
factorial =1
for i in range(number,1,-1):
    factorial = factorial*i
print("factorial of ",number,"! = ",factorial)


####9 print numbers from 1 to 100 and print only those numbers that are greater than 50 and divisible by 4(use nested if)

for i in range(1,101):
    if i>50:
        if i%4==0:
            print(i)
       # else:
           # print("not divisible by 4")
    #else:
        #print("number is less than equal to 50")

#ORRR
for i in range(1,101):
    if i>50 and i%4==0:        
        print(i)
     


####10 print numbers from 1 to 100 and count how many numbers are divisible by 5

count=0
for i in range(1,101):
    if i %5==0:
        count+=1
print(" numbers divisible by 5 between 1 to 100 is:-",count)