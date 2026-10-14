guess=int(input("Guess a number: "))
attempts=1
secret=7
while guess!=secret:
    if guess>secret:
        print("Too high")
        print("Try Again")
        guess=int(input("Guess a number: "))
    elif guess<secret:
        print("Too Low")
        print("Try Again")
        guess=int(input("Guess a number: "))
    attempts=attempts+1
print("You guessed it")
print(f"Total attempts : {attempts}")