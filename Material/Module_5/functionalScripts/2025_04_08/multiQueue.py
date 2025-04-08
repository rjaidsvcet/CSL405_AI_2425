from multiprocessing import Queue, Process

def square (inputNumber, queue):
    for n in inputNumber:
        queue.put (n*n)

def makeNegatives (inputNumber, queue):
    for i in inputNumber:
        queue.put (-1 * i)

if __name__ == '__main__':
    numbers = range (1, 10)
    q = Queue ()

    firstProcess = Process (target=square, args=(numbers, q))
    secondProcess = Process (target=makeNegatives, args= (numbers, q))

    firstProcess.start ()
    secondProcess.start ()

    firstProcess.join ()
    secondProcess.join ()

    while not q.empty ():
        print (q.get ())
