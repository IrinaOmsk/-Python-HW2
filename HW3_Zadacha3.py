#3. Задайте список из n чисел последовательности (1+1/n)^n 
# и выведите на экран их сумму.
num = int(input("Введите число "))
lst = []
for i in range(1, num + 1):
    lst.append((1 + 1 / i)**i)
print(lst)
print(sum(lst))
