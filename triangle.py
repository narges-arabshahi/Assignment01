a=float(input("please enter side1: "))
b=float(input("please enter side2: "))
c=float(input("please enter side3: "))
if a+b>c and a+c>b and b+c>a:
    print("these inputs can build a triangle")
else:
    print("these input cannot build a triangle")