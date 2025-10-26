#Find all duplicate characters in a string
def findDuplicates(string):
    lst1 = []
    lst2 = []

    for i in range(len(string)):
        count = 1
        for j in range(len(string)):
            if i!=j and string[i] == string[j]:
                count += 1
        if count > 1:
            lst1.append(string[i])
    for value in lst1:
        if value not in lst2:
            lst2.append(value)
    return lst2

duplicate = findDuplicates("programming")
print("Duplicate value in the string:",duplicate)


            
