#pasword checker
password = input("tell the password : ")
def pass_analyzation(password):
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    has_length = False 

    for i in password:
        if i.isupper():
            has_upper = True
        elif i.islower():
            has_lower = True
        elif i.isdigit():
            has_digit = True
        else:
            has_special = True 
    if len(password) >= 8:
        has_length = True
    criteria = [has_lower, has_upper, has_digit, has_special, has_length]
    total = sum(criteria)
    if total <= 2:
        print("Pass is weak")
    elif total == 3:
        print("its normal")
    else:
        print("its strong")

pass_analyzation(password)