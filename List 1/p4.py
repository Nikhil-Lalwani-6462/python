#get the smallest number from a list.
def getSmallest(lst):
    min = 100
    for value in lst:
        if value < min:
            min = value
    return min

Minimum = getSmallest([4, 7, 1, 9, 3])
print("Smallest value in the list:",Minimum)

