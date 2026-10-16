digits=1234
total=0
while digits>0:
    last_digit=digits%10
    total=total+last_digit
    remove_digit=digits//10
    digits=remove_digit
print(total)