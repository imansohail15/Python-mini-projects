num=int(input("Enter your number: "))
even_sum=0
odd_sum=0
for i in range(1,num+1):
    if i%2==0:
        even_sum=even_sum+i
    elif i%2!=0:
        odd_sum=odd_sum+i
        
print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")