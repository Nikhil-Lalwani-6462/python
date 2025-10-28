# Remove elements from a list at user-provided indexes.
def removeElements(colors):
    index = input("Enter space-seperated indexes to remove the item from the List:")
    lst = index.split()
    lst.sort(reverse=True)
    for value in lst:
        int_value = int(value)
        colors.pop(int_value)
    return colors
        
AfterRemoved = removeElements(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'])
print("After remove colors from the list:",AfterRemoved)

