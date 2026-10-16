original_num=123
num=123
reverse=0
while num>0:
    last_digit=num%10
    reverse=reverse*10 + last_digit
    remove_digit=num//10
    num=remove_digit
print(f"The reverse of {original_num} is {reverse}")