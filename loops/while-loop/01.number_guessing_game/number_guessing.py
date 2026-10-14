guess=int(input("Guess a number: "))
secret=7
i=0
while guess!=secret:
    print("Try Again")
    guess=int(input("Guess a number: "))
    i=i+1
print("You guessed it")