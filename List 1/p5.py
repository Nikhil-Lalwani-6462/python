# count the number of strings in a list where the string length is 2 or more and the first and last characters are the same
def countNumber(lst):
    count = 0
    for value in lst:
        value.lower()
        if len(value) >= 2 and value == value[::-1]:
            count += 1
    return count

countValues = countNumber( ['abc', 'xyz', 'aba', '1221'])
print("the number of strings in a list where the string length is 2 or more and the first and last characters are the same:",countValues)
