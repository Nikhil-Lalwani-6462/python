#Extract all numbers from a mixed list
def extractList(lst):
    new_lst = []
    for value in lst:
        if type(value) != str:
            new_lst.append(value)

    return new_lst

ExtractList = extractList(['hello', 42, 3.14, 'world', 7])
print("After extracting the list:",ExtractList)
