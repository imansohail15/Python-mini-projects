expense1=int(input("Enter your first expense: "))
expense2=int(input("Enter your second expense: "))
expense3=int(input("Enter your third expense: "))
total_expense=expense1+expense2+expense3
print(f"Your Total Expense is {total_expense}")
if total_expense>5000:
    print("High spending")
else:
    print("Spending is under control")