#.Merge two dictionaries
def mergeDictionary(diction1,diction2):
    merged = diction1 | diction2
    return merged

Merged = mergeDictionary({'a': 1},{'b': 2})
print("After Merged:",Merged)
