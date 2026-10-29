word1=input("Enter first word: ")
word2=input("Enter second word: ")
word1=word1.lower()
word2=word2.lower()
if sorted(word2)==sorted(word1):
    print("Anagrams")
else:
    print("Not Anagrams")