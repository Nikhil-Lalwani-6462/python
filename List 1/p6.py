# remove duplicates from a list.
def removeDuplicates(lst):
    new_lst = []
    for value in lst:
        if value not in new_lst:
            new_lst.append(value)
    return new_lst

Unique = removeDuplicates([1, 2, 2, 3, 4, 4, 5])
print("After removing duplicate value from the list:",Unique)
