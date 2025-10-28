def addKeyValue(diction):
    while True:
        key = input("Enter key (alphabets): ")
        try:
            value = float(input("Enter value (number): "))
        except ValueError:
            print("Invalid number! Try again.")
            continue
        
        # add or update the dictionary
        diction.update({key: value})
        print("Updated dictionary:", diction)
        
        # ask user if they want to continue
        choice = input("Do you want to add another key-value pair? (yes/no): ").lower()
        if choice in ("no", "n", "false"):
            break
    
    return diction

# initial dictionary
Key_Value = addKeyValue({'a': 1, 'b': 2})
print("Final dictionary:", Key_Value)
