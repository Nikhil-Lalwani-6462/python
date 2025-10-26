#.Remove all characters except alphabets from a string
def exceptAlphabets(string):
    new_string = ""
    for char in string:
        if char.isalpha():
            new_string += char
    return new_string

alphabets = exceptAlphabets("H3ll0! #Python123")
print("Filtered string with only alphabets",alphabets)


