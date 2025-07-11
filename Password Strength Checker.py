import getpass

lowercase_letters = [chr(x) for x in range(ord('a'), ord('z')+1)]
uppercase_letters = [chr(X) for X in range(ord('A'), ord('Z')+1)]
numbers = [str(n) for n in range(10)]
print(numbers)
special_characters = list("!@#$%^&*()-_=+[]{};:'\",.<>?/|\\")

def intersection(list1, list2):
    if list(set(list1) & set(list2)) == []:
        return False
    else: return True

def strength(passwd):
    L = list(passwd)
    
    count = int(intersection(passwd, lowercase_letters)) + \
            int(intersection(passwd, uppercase_letters)) + \
            int(intersection(passwd, numbers)) + \
            int(intersection(passwd, special_characters)) + \
            int(len(L) >= 12)
    
    if count == 5:
        return 'Strong password'
    elif count >=3 and len(L) >= 8:
        return 'Moderate password'        
    else:
        return 'Weak password'

passwd = getpass.getpass("Enter the password (it'd be invisible): ")
# I added this library to make the password invisible when typing it, 
# just like on linux command line

print(f'The password {passwd} is a {strength(passwd)}')
# In this print function, the password shouldn't be shown at all 
# because the point of all this is for it to be hidden, but 
# I added it just to understand how the code works

