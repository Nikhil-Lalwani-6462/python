#Write a Python program to flatten a nested list
def flattenList(lst):
    Flattened = []
    for value in lst:
        if type(value) == list:
            for inner_value in value:
                Flattened.append(inner_value)
        else:
            Flattened.append(value)
    return Flattened

Flattened = flattenList( [[1, 2], [3, 4], [5]])
print("After Flatten the list",Flattened)