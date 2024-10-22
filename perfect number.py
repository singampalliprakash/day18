num=int(input("enter the number:"))
sum=0
for i in range(1,num):
    if (num%i==0):
        sum=sum+i
if num==sum:
    print(f"it is a perfect number{num}")
else:
    print("it is not a perfect number")
