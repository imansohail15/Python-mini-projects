num=int(input("Enter a number: "))
original_num=num
saved_num=num
count=0
total=0
while original_num>0:
    last_digit=original_num%10
    count=count+1
    remove_digit=original_num//10
    original_num=remove_digit
print(count)
while num>0:
    last_digit=num%10
    digits=last_digit**count
    total=total+digits
    remove_digit=num//10
    num=remove_digit
if total==saved_num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
    