#Create a dictionary from user input of 3 key-value pairs
def key_value():
    diction = {}
    try:
        no = eval(input("How many key-value you want to insert into the list"))
    except Exception as e:
        print(e)
    else:
        for i in range(no):
            key = input("Enter key as aphabets:")
            value = eval(input("Enter value as number:"))
            diction[key] = value
    return diction

diction = key_value()
print("Dictionary by the user input as key-value:",diction) 
