#two wheeler,four wheeler problem
age=int(input())
if age>18 and age<24:
    print("two wheeler")
elif age>24 and age<45:
    print("two and four wheeler")
elif age>45:
    print("all")
else:
    print("not")