#replace all spaces in a string with underscores
def replaceSpaces(string):
    new_string = ""
    for char in string:
        if char == " ":
            new_string += "_"
        else:
            new_string += char
    return new_string
    
replaceSpaces = replaceSpaces("Python is fun")
print("After Removing spaces from the string:",replaceSpaces)
