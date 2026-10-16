num=int(input("Enter your number: "))
original_num= num
reverse=0
while num>0:
    last_digit=num%10
    reverse=reverse*10 + last_digit
    remove_digits=num//10
    num=remove_digits
if reverse==original_num:
    print("It is palindrome")
else:
    print("It is not palindrome")
