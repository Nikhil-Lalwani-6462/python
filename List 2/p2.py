#Write a Python program to split a list into two halves.
def twoHalves(lst):
    len_two_halves = len(lst)//2
    lst1 = []
    lst2 = []

    for i in range(len_two_halves):
        lst1.append(lst[i])

    for j in range(len_two_halves,len(lst)):
        lst2.append(lst[j])

    return (lst1,lst2)

TwoHalves = twoHalves([10, 20, 30, 40, 50, 60])
print("After divinding list into two halves",TwoHalves)
