#Delete a key from a dictionary
def delKey(diction,key):
    if key in diction:
        value = diction.pop(key)
        return diction
    else:
        return "No key found in the dictionary"

updated = delKey( {'a': 1,'b': 2},'b')
print("After Operation:",updated)

    

