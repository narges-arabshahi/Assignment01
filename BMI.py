w=float(input("please enter your weight(kg): "))
h=float(input("please enter your height(m): "))
bmi=w/h**2
if bmi< 18.5:
    result="Underweight"
if bmi>=18.5 and bmi<=24.9:
    result="Normal"
if bmi>=25 and bmi<=29.9:
    result="Overweight"
if bmi>=30 and bmi<=34.9:
    result="Obese"
if bmi>35:
    result="extremely obese"
print(result)