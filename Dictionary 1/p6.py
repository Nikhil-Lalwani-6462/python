#Update the value of an existing key in a dictionary
def updateValue(diction):
    diction['a'] = 100
    return diction
UpdatetedValue = updateValue({'a':1,'b':2})
print("AFter updating the dictionary:",UpdatetedValue)
