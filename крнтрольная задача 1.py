#Задача 1
def card(a):
    for i in a:
       return '*'*12+a[-4:]
a=input('Введите номер карты:')

print(card(a))