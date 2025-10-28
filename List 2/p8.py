#count the frequency of elements in a list and return it as a dictionary
def countFrequency(lst):
    diction = {}
    count = 0
    for i in range(len(lst)):
        count = 1
        for j in range(len(lst)):
            if i!=j and lst[i] == lst[j]:
                count += 1
                diction[lst[i]] = count
        diction[lst[i]] = count
    return diction


CountFrequency = countFrequency([1, 2, 2, 3, 1, 4, 2])
print("After count the frequency in the list:",CountFrequency)

