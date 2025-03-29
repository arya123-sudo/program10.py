num1=int(input("enter a number: "))
if(num1>0 and num1%2==0):
   print("It is positive even ") 
elif(num1<0 and num1%2==0):
    print("It is negative even")
elif(num1>0 and num1%2!=0):
    print("it is positive odd ")
elif(num1<0 and num1%2!=0):
    print("it is negative odd")           
else:
    print("it is zero")