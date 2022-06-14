import math
a=float(input("please enter first number "))
b=float(input("please enter second number "))
op=input("please enter your operation ")
if op=="+":
    result=a + b 
elif op=="-":
    result=a - b
elif op=="*":
    result=a * b 
elif op=="/":
    if b!=0:
        result=a / b
    else :
        result="can not divide by zero"
elif op=="radical":
    result=math.sqrt(a)
elif op=="fact":
    result=math.factorial(a)
elif op=="sin":
    result=math.sin(math.radians(a))
elif op=="cos":
    result=math.cos(math.radians(a))
elif op=="tan":
    result=math.tan(math.radians(a))
elif op=="cot":
    result=math.cos(math.radians(a))/math.sin(math.radians(a))
print(result)
