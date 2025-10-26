#Check if a string contains only digits
def onlyDigits(string):
    for char in string:
        if not char.isdigit():
            return False
    return True

OnlyDigit = onlyDigits("12345")
print(OnlyDigit)