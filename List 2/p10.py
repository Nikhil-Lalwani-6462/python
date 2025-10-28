#Find the index of all occurrences of an element
def findIndex(lst,element):
    new_lst = []
    string = "No element found in the list"
    if element in lst:
        for i in range(len(lst)):
            if lst[i] == element:
                new_lst.append(i)
    else:
        return string
    

    return new_lst
Index = findIndex([1, 2, 3, 2, 4, 2, 5],9)
print("Index of the element in the list:",Index)
