num1=int(input("Enter first number :"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number :"))
if((num1>num2) and (num1>num3)):
    print("num1=",num1,">","num2 and num3")
elif((num2>num1) and (num2>num3)):
    print("num2=",num2,">","num1 and num3")
else:
    print("num3=",num3,">","num1 and num2")
