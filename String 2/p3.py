#Check if two strings are rotations of each other
def checkRotations(string1,string2):
    isRotate = False
    if string1[:2:] == string2[2::] and string1[2::] == string2[:2:]:
        isRotate = True
    return isRotate


isRotate = checkRotations("abcd", "cdab")
print("String is rotate to each other.?",isRotate)
