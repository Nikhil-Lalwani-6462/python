#Check if a key exists in a dictionary
def checkKey(diction):
    try:
        check_key = input("Enter a Key to check whether it is in the dictionary or not:")
    except ValueError as ve:
        print(ve)
    else:
        for key in diction.keys():
            if key == check_key:
                print(check_key,"is in the list")
            else:
                print(check_key,"is not in the list")
                break
                

checkKey({'a': 1, 'b': 2})
