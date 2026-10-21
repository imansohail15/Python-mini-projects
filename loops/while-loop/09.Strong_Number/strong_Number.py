num=int(input("Enter a number: "))
saved_num=num
total=0
while num>0:
    last_digit=num%10
    fact=1
    i=last_digit
    while i>0:
        fact=fact*i
        i=i-1
    total=total+fact
    num=num//10
if total==saved_num:
    print("Strong Number")
else:
    print("Not a strong Number")