# find the common elements in two lists 
def commonElements(lst1,lst2):
    new_lst = []
    for value in lst1:
        if value in lst2:
            new_lst.append(value)
    return new_lst

CommonElements = commonElements( [1, 2, 3, 4], [3, 4, 5, 6])
print("Common elements from both the lists:",CommonElements)

