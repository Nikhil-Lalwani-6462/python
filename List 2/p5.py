#Write a Python program to rotate a list by k elements
def rotateList(lst):
    index = eval(input("Enter index to rotate the list from that index:"))
    new_list = lst[index:] + lst[:index]
    return new_list





Rotated = rotateList([1, 2, 3, 4, 5])
print("After Rotation",Rotated)
