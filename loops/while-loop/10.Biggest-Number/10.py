num=5832
largest=0
while num>0:
    last_digit=num%10
    if last_digit>largest:
        largest=last_digit
    num=num//10
print(largest)
    