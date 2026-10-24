def count_vowels(text):
    count=0
    for i in range(len(text)):
        if text[i] in "aeiouAEIOU":
            count=count+1
    print(count)
            
count_vowels("pineapple")