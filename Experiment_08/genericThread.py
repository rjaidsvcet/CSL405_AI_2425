import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(f"Thread 1 - Number: {i}")
        time.sleep(1)

def print_letters():
    for letter in 'ABCDE':
        print(f"Thread 2 - Letter: {letter}")
        time.sleep(1)

def print_squares():
    for i in range(1, 6):
        print(f"Thread 3 - Square of {i}: {i ** 2}")
        time.sleep(1)

# Creating threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)
thread3 = threading.Thread(target=print_squares)

# Starting threads
thread1.start()
thread2.start()
thread3.start()

# Ensuring all threads complete
thread1.join()
thread2.join()
thread3.join()

print("All threads have finished executing.")