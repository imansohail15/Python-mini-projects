word=input("Enter a word: ")
count=0
for i in range(0,len(word)):
    if word[i] in "aeiouAEIOU":
        count=count+1
print(count)