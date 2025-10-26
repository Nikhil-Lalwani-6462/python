#Count the frequency of each character in a string
def countFrequency(string):
    count = 0
    diction = {}
    for i in range(len(string)):
        count = 1 
        for j in range(len(string)):
            if i!=j and string[i] == string[j]:
                count += 1
                diction[string[i]] = count
        diction[string[i]] = count
    return diction

diction = countFrequency("banana")
print("Count of frequency in the string is:",diction)


