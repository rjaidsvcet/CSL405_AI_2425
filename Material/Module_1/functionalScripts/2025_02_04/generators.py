import sys

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

y = map (lambda i : i**2, x)

print (y.__next__ ())
print (y.__next__ ())
print (y.__next__ ())

# print (next (y))
# print (next (y))
# print (next (y))
# print ('For loop starts')
# for i in y:
#     print (i)

# print (f'Size of x : {sys.getsizeof (list (y))}')
# print (f'Size of range : {sys.getsizeof (y)}')

# print (list (y))

# for i in y:
#     print (i)

# print (f'Size of x : {sys.getsizeof (x)}')
# print (f'Size of range : {sys.getsizeof (range (1, 11))}')

# for element in x:
#     print (element)

# for i in range (1, 11):
#     print (i)