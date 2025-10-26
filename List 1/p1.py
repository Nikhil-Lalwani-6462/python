#sum all the items in a list
def sumItems(lst):
    sum = 0
    for value in lst:
        sum += value
    return sum

SumOfValues = sumItems([1,2,3,4,5])
print("Sum of values in the list:",SumOfValues)


    