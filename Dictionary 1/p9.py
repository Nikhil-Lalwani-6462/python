#Sort dictionary keys alphabetically
def sortAlphabetically(diction):
    new_diction = {}
    for k in sorted(diction.keys()):
       new_diction[k] = diction[k]
    return new_diction    
    
Sorted = sortAlphabetically({'b': 2, 'a': 5, 'c': 1})
print("After sorting:",Sorted)