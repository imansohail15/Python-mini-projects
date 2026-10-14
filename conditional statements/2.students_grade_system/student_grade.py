bio=int(input("Enter your marks: "))
chem=int(input("Enter your marks: "))
phy=int(input("Enter your marks: "))

if (bio<0 or bio>100) or (chem<0 or chem>100) or (phy<0 or phy>100):
        print("invalid marks")
else:
    total_marks=300
    obt_marks=bio+chem+phy
    percentage=(obt_marks/total_marks)*100
    print(f"Obtained Marks: {obt_marks}/{total_marks}")
    print(f"Percentage: {percentage}%")
    if percentage>=80:
        grade="A"
        print("Pass")
    elif percentage>=70:
        grade="B"
        print("Pass")
    elif percentage>=60:
        grade="C"
        print("Pass")
    elif percentage>=50:
        grade="D"
        print("Pass")
    else:
        grade="F"
        print("Fail")
    print(f"Grade: {grade}")