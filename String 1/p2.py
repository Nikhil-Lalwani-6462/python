# calculate the length of a string (without using len())
def calculateLength(string):
    count = 0
    for char in string:
        count += 1
    return count


LengthOfString = calculateLength("Hello")
print("Length of the string is:",LengthOfString)