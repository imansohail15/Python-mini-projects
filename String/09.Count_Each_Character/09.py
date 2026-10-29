word=input("Enter a string: ")
count=0
checked=""
for i in range(0,len(word)):
    if word[i] not in checked:
        count=word.count(word[i])
        print(f"{word[i]} : {count}")
        checked=checked+word[i]