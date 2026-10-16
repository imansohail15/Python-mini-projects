digits=int(input("Enter digits: "))
count=0
while digits>0:
    last_digit=digits%10
    count=count+1
    remove_digit=digits//10
    digits=remove_digit
print(count)