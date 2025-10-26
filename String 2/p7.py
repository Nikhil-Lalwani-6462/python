#Remove all vowels from a string
def removeVowels(string):
    new_string = ""
    vowels = "aeiouAEIOU"
    for char in string:
        if char not in vowels:
            new_string += char
    return new_string

VowelsRemoved = removeVowels("Hello World")
print("After removing vowels:",VowelsRemoved)
    