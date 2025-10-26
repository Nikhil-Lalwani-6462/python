#Check if a string has all unique characters
def checkUnique(string):
    count = 0 
    for i in range(len(string)):
        count = 1
        for j in range(len(string)):
            if i != j and string[i] == string[j]:
            
                count += 1
            if count != 1:
                return False
    return True
    

            
isUnique = checkUnique("hello")
print(isUnique)

