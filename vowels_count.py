string = "aeroplane"
wordList = string.split()
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for word in wordList:
    vowelCount = 0
   
    for i in range(0, len(word)):
       
        if word[i] in vowels:
            vowelCount += 1
    print("The word is", word, "contains", vowelCount, "vowels")