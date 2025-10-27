# find the second largest number in a list.
def secondLargest(lst):
    max_1 = 0
    max_2 = 0
    for value in lst:
        if value > max_1:
            max_2 = max_1
            max_1 = value
        elif value > max_2:
            max_2 = value
    return max_2


SecondLargest = secondLargest([4, 1, 7, 3, 9, 5])
print("Second Largest element from the list:",SecondLargest)


