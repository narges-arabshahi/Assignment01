name=input("please enter your name: ")
family=input("please enter your family")
score1=float(input("please enter your score1: "))
score2=float(input("please enter your score2: "))
score3=float(input("please enter your score3: "))
average=(score1+score2+score3)/3
if average>=17:
    print("Great")
if average<17 and average>=12:
    print("Normal")
if average<12:
    print("Fail")