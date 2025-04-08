from multiprocessing import Process, Value, Lock, Array
from time import sleep

def addHundreds (inputNumber, lock):
    for _ in range (100):
        sleep (0.01)
    #     ### For Array
        for i in range (len (inputNumber)):
            with lock:
                inputNumber[i] += 1

        ### For value
        # lock.acquire ()
        # inputNumber.value += 1
        # lock.release ()
        # with lock:
        #     inputNumber.value += 1

if __name__ == '__main__':
    lock = Lock ()

    sharedArray = Array ('d', [0.0, 100.0, 200.0])
    # sharedNumber = Value ('i', 0)
    # print (f'Number at the beginning : {sharedNumber.value}')
    print (f'Number at the beginning : {sharedArray[:]}')

    firstProcess = Process (target=addHundreds, args=(sharedArray, lock))
    secondProcess = Process (target=addHundreds, args=(sharedArray, lock))
    # firstProcess = Process (target=addHundreds, args=(sharedNumber, lock))
    # secondProcess = Process (target=addHundreds, args=(sharedNumber, lock))

    firstProcess.start ()
    secondProcess.start ()

    firstProcess.join ()
    secondProcess.join ()

    # print (f'Value in the end : {sharedNumber.value}')
    print (f'Value in the end : {sharedArray[:]}')
