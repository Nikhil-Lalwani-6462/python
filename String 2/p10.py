#Replace multiple spaces in a string with a single space
def replaceSpaces(string):
    new_string = ""
    words = string.split()
    for char in words:
        new_string += char + " "
    return new_string


removeMultiple = replaceSpaces("Python  is  great")
print("After removing multiple spaces:",removeMultiple)

