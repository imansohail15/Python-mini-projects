word=input("Enter a word: ")
character=input("Enter a character: ")
count=0
for i in range(0,len(word)):
    if word[i]==character:
        count=count+1
print(count)