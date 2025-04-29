import getpass

lowercase_letters = [chr(x) for x in range(ord('a'), ord('z')+1)]
uppercase_letters = [chr(X) for X in range(ord('A'), ord('Z')+1)]
numbers = [n for n in range(10)]
special_characters = list("!@#$%^&*()-_=+[]{};:'\",.<>?/|\\")

def intersection(list1, list2):
    if list(set(list1) & set(list2)) == []:
        return False
    else: return True

def strength(passwd):
    L = list(passwd)
    
    count = int(intersection(passwd, lowercase_letters)) + int(intersection(passwd, uppercase_letters)) \
    + int(intersection(passwd, numbers)) + int(intersection(passwd, special_characters)) + int(len(L) >= 12)
    
    if count == 5:
        return 'Strong password'
    else if: scr >=3
        
        
    else:
        return 'Weak password'

passwd = getpass.getpass("Enter something: ")
print(f'{passwd}')
print(special_characters)
