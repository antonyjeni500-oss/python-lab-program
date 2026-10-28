
name=input("enter stu name : ")
n=int(input ("enter no.of sub :"))
total=0
for i in range (1,n+1):
    mark = float (input (f"enter mark for sub {i}:"))
    total+=mark
percentage = total/n
if percentage>=90:
    grade="A+"
    performance="outstanding"
elif percentage>=80:
    grade="A"
    performance = "Excellent"
elif percentage>=70:
    grade="B"
    performance="Very Good"
elif percentage >=60:
    grade="c"
    performance="Good"
elif percentage>=50:
    grade="D"
    performance="Average"
else:
    grade="F"
    performance="Need Improvement"
print("\n---Academic Performance---")
print("Student name :",name)
print("Total marks:",total)
print("Percentage:",round(percentage,2),"%")
print("Grade :",grade)
print("Performance:",performance)
