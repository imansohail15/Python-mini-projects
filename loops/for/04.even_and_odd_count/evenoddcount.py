num=int(input("Enter a number: "))
even_count=0
odd_count=0
for i in range(1,num+1):
    if i%2==0:
        even_count +=1
    elif i%2!=0:
        odd_count +=1
print(f"Even: {even_count}")
print(f"Odd: {odd_count}")