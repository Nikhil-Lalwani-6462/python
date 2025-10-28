#Write a Python function that takes two lists and returns True if they have at least one common member.
def commonValue(lst1,lst2):
    for value in lst2:
        if value in lst1:
            return True
isCommon = commonValue( [1, 2, 3], [5, 6, 2])
print("Give true if there is any common value in both else false:",isCommon)
