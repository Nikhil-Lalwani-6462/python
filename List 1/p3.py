# get the largest number from a list.
def getLargest(lst):
    max = 0
    for value in lst:
        if value > max:
            max = value
    return max

Largest = getLargest([4, 7, 1, 9, 3])
print("Largest number in the list:",Largest)
