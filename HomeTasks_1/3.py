'''
Используя один оператор вывода print, программа должна напечатать прямоугольный
треугольник из символов знака плюс *
'''

var = int(input("Enter a number of *: "))
for i in range(1, var + 1):
  print("*" * i)