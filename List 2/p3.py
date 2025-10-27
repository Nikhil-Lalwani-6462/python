#Write a Python program to remove all even numbers from a list.
def removeEven(lst):
    for value in lst:
        if value%2 == 0:
            lst.remove(value)
    return lst

RemoveEven = removeEven([1, 2, 3, 4, 5, 6, 7, 8])
print("After removing even numbers from the list:",RemoveEven)
