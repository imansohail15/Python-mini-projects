guess=int(input("Guess a number: "))
attempts=1
secret=7
i=0
while guess!=secret:
    print("Try Again")
    guess=int(input("Guess a number: "))
    attempts=attempts+1
    i=i+1
print("You guessed it")
print(f"Total attempts : {attempts}")