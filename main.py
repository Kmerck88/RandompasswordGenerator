import random, string


def password(length, num=False, strength='weak'):
    """length of password, num if you want a number, 
    and strength(weak, strong, very)"""
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    letter = lower + upper
    dig = string.digits
    punct = string.punctuation
    pwd = ''
    if strength == 'weak':
        if num:
            length -= 2
            for i in range(2):
                pwd += random.choice(dig)
        for i in range(length):
            pwd += random.choice(lower)
    return pwd


print(password(5,num=True))
