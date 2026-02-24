num1=int(input("Enter the first number:"))
num2=int(input("Enter second number:"))
op=input("ENTER operator(+,-,*,/):")

if op=="+":
    result=num1+num2
elif op=="-":
    result=num1-num2
elif op=="*":
    result=num1*num2
elif op=="/":
    if num2!=0:
        result=num1/num2
    else:
         print("Division by zero is not allowed")
         exit()
else:
    print("Invalid operator")
    exit()

print("Result =",result) 

if result>0:
    print("The result is positive")
elif result<0:
    print("The result is negative")
else:
    print("The result is zero")