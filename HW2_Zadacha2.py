#2. Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
num = int(input("Введите число "))
for i in range(1, num + 1):
    res = 1
    for j in range(1, i + 1):
        res = res * j
    print(res, end=" ")
print()
