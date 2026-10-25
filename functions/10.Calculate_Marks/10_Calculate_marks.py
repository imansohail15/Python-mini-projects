def calculate_marks(phy,chem,bio):
    Total_marks=300
    obtained_marks=phy+chem+bio
    percentage=(obtained_marks/Total_marks)*100
    if percentage>=90:
        Grade = "A"
    elif percentage>=80:
        Grade = "B"
    elif percentage>=70:
        Grade = "C"
    elif percentage>=60:
        Grade = "D"
    elif percentage>=50:
        Grade = "E"
    else:
        Grade = "F"
    return obtained_marks,percentage,Grade
    
print(calculate_marks(90,60,23))