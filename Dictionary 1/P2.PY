#.Print all keys from a dictionary
def printKeys(diction):
    lst = []
    for key in diction.keys():
        lst.append(key)

    return lst
Lst = printKeys({'a': 1, 'b': 2, 'c': 3})
print("Keys in he dictionary:",Lst)


