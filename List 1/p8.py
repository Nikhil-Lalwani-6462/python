#.Write a Python program to clone or copy a list.
def copyList(lst):
    copied_lst = []
    copied_lst = lst.copy()
    return copied_lst

copied = copyList([1,2,3])
print("After copy:",copied)
