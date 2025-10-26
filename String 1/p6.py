# find the frequency of each character in a string
def findFrequency(string):
    diction = {}
    count = 0
    for i in range(len(string)):
        count = 1
        for j in range(len(string)):
            if i!=j and string[i] == string[j]:
                count += 1
                diction[string[i]]=count
            diction[string[i]] = count
    return diction

findFrequency = findFrequency("banana")
print(findFrequency)