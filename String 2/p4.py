# Find the first non-repeating character in a string
def firstNonRepeating(string):
    count = 0
    for i in range(len(string)):
        count = 0
        for j in range(len(string)):
            if i!=j and string[i] == string[j]:
                count += 1
        if count == 0:
            return string[i]


firstNonRepeating = firstNonRepeating("aabbcdeff")
print("First Non Repeating character in the string:",firstNonRepeating)
    