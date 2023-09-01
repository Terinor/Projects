# def fibonacci(n):
    
    
#     if i == n:
#         return fibo
#     else:
#         fibo = fibonacci(n) - fibonacci(n-1)
#         i += 1
# print (fibonacci(6))


# def factorial(n):
#     if n < 2:
#         return 1  # Базовий випадок
#     else:
#         return n * factorial(n - 1)  # Рекурсивний випадок

def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
print( fibonacci_recursive(40))