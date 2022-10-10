# Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный.
# Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;

summ = lambda a, b : a + b
mult = lambda a, b : a * b
sub = lambda a, b : a - b
div = lambda a, b : a / b

def result(op, a, b):
    print(op(a,b))

result(summ, 10, 9)
result(mult, 10, 9)
result(sub, 10, 9)
result(div, 10, 9)

