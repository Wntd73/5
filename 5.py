'''Задана рекуррентная функция. Область определения функции – натуральные числа. Написать 
программу сравнительного вычисления данной функции рекурсивно и итерационно. Определить границы 
применимости рекурсивного и итерационного подхода. Результаты сравнительного исследования 
времени вычисления представить в табличной форме. Обязательное требование – минимизация времени 
выполнения и объема памяти.
Вариант 23. F(1) = 1, F(2) = 1, F(n) = (-1)^n*(F(n-2)*(n-1)/(2n)! + 2), при n > 2'''
from math import factorial
import timeit
fact = 2*3*4
n=input('Введите натуральное число n > 1 и n < 996: ')
while True:
    try: n = int(n)
    except: n = input('Вы неправильно ввели n. Введите натуральное число n > 1 и n < 996: ')
    else: 
        if n>1 and n<996: break
        else: n = input('Вы неправильно ввели n. Введите натуральное число n > 1 и n < 996: ')
def st1(n):
    if n%2==0: return 1
    else: return -1
def recursive_f(n):
    if n==1 or n==2: return 1
    else: return st1(n) * (recursive_f(n-2) + (n-1) / factorial(2*n)+2)    
def iterative_f(n, fact):
    f2,f1=1,1
    for i in range(3,n+1):
        fact *= (i*2) * ((i*2)-1)
        f = st1(i) * (f2 + (i-1)/fact+2)   
        f2,f1=f1,f  
        
    if n==1 or n==2: f=f2          
    return f
def compare_methods(n):
    print(f"n: {n}")
    a = timeit.timeit('recursive_f(n)', globals = globals(), number =1)
    print(f'Рекурсивный результат: {recursive_f(n)} \nВремя рекурсивного вычисления: {a}')
    a = timeit.timeit('iterative_f(n, fact)', globals = globals(), number =1)
    print(f'Итерационный результат: {iterative_f(n, fact)} \nВремя итерационного вычисления: {a}')
compare_methods(n)