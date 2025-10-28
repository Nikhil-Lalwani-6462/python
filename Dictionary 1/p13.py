#Create a nested dictionary [through user input.]
def nestedDictionary():
    
    try:
        no = eval(input("Enter Number of employees you want to insert into the dictionary:"))
    except ValueError:
        print("Enter type as a number instead of any other type")
    else:
        
        

        for i in range(no):
            super_diction = {}
            sub_diction = {}
            name = input("Enter a name of the employee:")
            sub_diction['name'] = namecd 
            age = eval(input("Enter the age of the employee:")) 
            sub_diction['age'] = age
            super_diction['emp'] = sub_diction
    return super_diction

Nested = nestedDictionary()
print("Nested Dictionary:",Nested)

