#Create a dictionary from two lists
def createDictionary(lst1,lst2):
    diction = {}
    for i in range(len(lst1)):
        diction[lst1[i]] = lst2[i]

    return diction
Created = createDictionary(['a', 'b'], [1, 2])
print("Created dictionary from two list:",Created) 
