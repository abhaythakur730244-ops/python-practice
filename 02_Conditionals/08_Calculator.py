num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the Second number :"))

print("For Addition use +")
print("For Subtraction use -")
print("For Multiplication use *")
print("For Division use /")
print("For Reminder use %")
operation = input("Enter the Operation :")

if operation == '+':
    print(num1+num2)
elif operation == '-':
    print(num1-num2)
elif operation == '*':
    print(num1*num2)
elif operation == '/':
    print(num1/num2)
elif operation == '%':
    print(num1%num2)
else:
    print("SomeThing is Wrong")

