import os

files = [f for f in os.listdir('.') if os.path.isfile(f)]

print("Files in the current directory:")
for file in files:
    print(file)

'''
The above scipt uses os module to perform the required function.
Utilize the pathlib module to perform the same functionality.
'''