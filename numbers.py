#picoCTF The Numbers Cryptography Challenge

from string import ascii_uppercase

flag =[]

numbers = [16, 9, 3, 15, 3, 20, 6, '{', 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14, '}']

for number in numbers:
    if type(number) == str:
        flag.append(number)
    else:
        flag.append(ascii_uppercase[number-1])

print(''.join(flag))



