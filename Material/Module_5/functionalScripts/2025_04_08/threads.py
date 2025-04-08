import time
from threading import Thread
import concurrent.futures

start = time.perf_counter ()

def doSomething (seconds):
    print (f'Process is sleeping for {seconds}')
    time.sleep (seconds)
    return 'Process is done sleeping'


# firstThread = Thread (target=doSomething)
# secondThread = Thread (target=doSomething)

# firstThread.start ()
# secondThread.start ()

# firstThread.join ()
# secondThread.join ()

# threads = list ()

# for _ in range (10):
#     t = Thread (target=doSomething, args=[1.5])
#     t.start ()
#     threads.append (t)

# for thread in threads:
#     thread.join ()

with concurrent.futures.ThreadPoolExecutor () as executor:
    # f1 = executor.submit (doSomething, 1)
    # print (f1.result ())
    seconds = [5, 4, 3, 2, 1]
    # results = [executor.submit (doSomething, sec) \
    #            for sec in seconds]
    
    # for f in concurrent.futures.as_completed (results):
    #     print (f.result ())
    results = executor.map (doSomething, seconds)

    for r in results:
        print (r)

end = time.perf_counter ()

print (f'Finished execution in {end-start} seconds')