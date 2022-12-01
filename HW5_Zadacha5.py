#5. Реализуйте алгоритм перемешивания списка.
from random import randint
lst = input("Введите список через пробел ").split()
for i in range(len(lst)):
    elem = lst.pop(randint(0, len(lst) - 1))
    lst.insert(randint(0, len(lst) - 1), elem)
print(lst)
