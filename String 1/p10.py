#count the number of words in a string
def countNumber(text):
    count = 1
    for char in text:
        if char == " ":
            count += 1
    return count

countNumbers = countNumber("Python is easy to learn")
print("Number of space in the text :", countNumbers)
