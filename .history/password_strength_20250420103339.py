import getpass

lowercase_letters = [chr(x) for x in range(ord('a'), ord('z')+1)]
uppercase_letters = [chr(X) for X in range(ord('A'), ord('Z')+1)]
numbers = [n for n in range(10)]
special_characters = list("!@#$%^&*()-_=+[]{};:'\",.<>?/|\\")

def strength(passwd):
    L = list(passwd)
    
    
    return 0

passwd = getpass.getpass("Enter something: ")
print(f'{passwd}')
