secret_number=7
guess=int(input("Enter your guess: "))
if guess==secret_number:
    print("Correct guess!")
elif guess<secret_number:
    print("Low!")
else:
    print("High")