# import time

# ## Usando listas
# fib = [1, 1]

# for i in range (10**4):
#     fib.append(fib[-1] + fib[-2])

# print(fib)
# print(len(fib))


#####################
## Usando recursao
# def fib(n):
#     if n <= 1:
#         return n
#     return (fib(n-2) + fib(n-1))

# for i in range(10**2):
#     print(fib(i))


















####################
## Usando recursao 2
# def fib(n, a = 0, b = 1):
#     if n == 0:
#         return a
#     if n == 1:
#         return b

#     return fib(n-1, b, a+b)

# l = []
# for i in range (500):
#     l.append(fib(i))

# print(l)
