#count the number of vowels in a string
def countVowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count


CountOfVowels = countVowels("Hello, How are You?")
print("Count of vowels is:", CountOfVowels)
    