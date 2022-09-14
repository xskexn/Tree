phrase = input("Phrase: ")
#testPhrase = "aeiou"
def vowelsCounter():
    count = 0  
    for c in phrase:
        if c in "aeiou":
            count += 1
    print(f"The number of vowels in your phrase is {count}")
vowelsCounter()