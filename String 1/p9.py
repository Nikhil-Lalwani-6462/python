#remove duplicate characters from a string
def removeDuplicateCharacters(string):
    new_string = ""
    for char in string:
        if char not in new_string:
            new_string += char
    return new_string 

removeDuplicateCharacters = removeDuplicateCharacters("programming")
print("After remove duplicate charactersv from the string is :",removeDuplicateCharacters)