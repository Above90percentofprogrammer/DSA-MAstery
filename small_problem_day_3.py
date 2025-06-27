# Check if a string contains only unique characters
str1 = input("tell the string you wanna add : ")

def unq_checker(str1):
    seem = set()
    for i in str1:
        if i in seem:
            return False
        else:
            seem.add(i)
    return True

if unq_checker(str1):
    print("Its unique......")
else:
    print("IT Has duplicates//.....")