# multiply all the items in a list by a specific number
def multiplyByNo(lst):
    multiply = 0
    new_lst = []
    for value in lst:
        multiply = value * 3
        new_lst.append(multiply)
    return new_lst

After_Update = multiplyByNo([2,4,6])
print("AFter multiply all values in the list by 3:",After_Update)
        
