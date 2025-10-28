#.Print all values from a dictionary
def printValues(diction):
    lst = []
    for value in diction.values():
        lst.append(value)
    return lst
Lst = printValues({'a': 1, 'b': 2, 'c': 3})
print("Values in the dictionary:",Lst)

