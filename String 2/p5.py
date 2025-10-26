#Count the number of words in a string (without using split())
def countSpace(string):
    count = 1
    for char in string:
        if char == " ":
            count += 1
    return count

countSpaces = countSpace("Python is fun")
print("Spaces in the Text :",countSpaces)
