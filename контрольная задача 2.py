# Задача 2

def word(a):
    if a==a[::-1]:
        print('Palindrom')
    else:
        print('Not Palindrom')
a=input('Slovo:')
word(a)