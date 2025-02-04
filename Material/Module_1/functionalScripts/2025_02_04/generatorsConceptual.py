import sys

def generatorFunction (n):
    for i in range (n):
        yield i ** 2

x = [i ** 2 for i in range (10000000)]
g = generatorFunction (10000000)

print (f'For list comprehension : {sys.getsizeof (x)}')
print (f'For generator function : {sys.getsizeof (g)}')