#sort a list of tuples by the second element.
def sortList(lst):
    tmp = 0
    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if lst[j][1] > lst[j+1][1]:
                tmp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = tmp
    return lst

SortedList = sortList([(1, 3), (2, 1), (4, 2)])
print("After sorting by second element:",SortedList)


