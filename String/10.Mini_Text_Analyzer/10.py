sentence=input("Enter a sentence: ")
print(f"Characters: {len(sentence)}")
print(f"Words: {len(sentence.split())}")
print(f"Reverse: {sentence[::-1]}")
count=0
for i in sentence:
    if i in "AEIOUaeiou":
        count=count+1
print(f"Total vowels: {count}")