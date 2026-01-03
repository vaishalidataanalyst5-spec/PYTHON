# 111111111111111

for i in range(3):
    for j in range(3):
        print("*",end="")
    print("\n")
              
#222222222222222

for i in range(4):
    for j in range(i):
        print("*",end="")
    print("\n")


#333333333333333

rows = int(input("enter the number of rows:"))
for i in range(rows+1,0,-1):
    for j in range(1,i):
        print("*",end="")
    print("\n")

#44444444444

rows = int(input("enter the number of rows:"))
for i in range(1,rows+1):
    for j in range(1,i*2):
        print("*",end ="")
    print("\n")

#555555555555555

rows = int(input("enter the number of rows:"))
for i in range(rows+1):
    for j in range(i*2):
        print("*",end ="")
    print("\n")

#666666666666666

rows = int(input("enter the number of rows:"))
for i in range(rows+1,0,-1):
    for j in range(i*2):
        print("*",end ="")
    print("\n")

#7777777777777777

rows = int(input("enter the number of rows:"))
for i in range(rows,0,-1):
    for j in range(1,i*2):
        print("*",end ="")
    print("\n")

#888888888888888888888

rows = int(input("enter the number of rows:"))
for i in range(rows+1,0,-1):
    for j in range(i*2):
        print("*",end ="")
    print("\n")

#999999999999999999999

rows = int(input("enter the number of rows:"))
for i in range(1,rows+1):
    for j in range(1,rows+1):
        if i==3:
            print("#",end="")
        else:
            print("*",end ="")
    print("\n")

#1000000000000000

rows = int(input("enter the number of rows:"))
for i in range(1,rows+1):
    for j in range(1,rows+1):
        print(i,end="")
        
    print("\n")

#11111111111111111111111

rows = int(input("enter the number of rows:"))
for i in range(1,rows+1):
    for j in range(1,rows+1):
        print(j,end=" ")
        
    print("\n")

#12222222222222222222222

rows = int(input("enter the number of rows:"))
for i in range(rows,0,-1):
    for j in range(rows):
        print(i,end=" ")
        
    print("\n")

#13333333333333333333333

rows = int(input("enter the number of rows:"))
for i in range(rows,0,-1):
    for j in range(rows,0,-1):
        print(j,end=" ")
        
    print("\n")