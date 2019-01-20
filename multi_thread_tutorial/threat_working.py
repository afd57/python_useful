'''
Thread tutorial
'''
import time
from threading import Thread
from multiprocessing.dummy import Pool as ThreadPool


def sleep_function(second):
    """
    Sleeping function
    for thread tutorial
    """
    print(f"sleeping {second} sec from thread {second}")
    time.sleep(second)
    print(f"finished sleeping from thread {second}")


if __name__ == "__main__":
    start_time = time.time()
    list_of_thread = set()
    for i in range(5, 15):
        t = Thread(target=sleep_function, args=(i,))
        list_of_thread.add(t)
        t.start()
    print('Threads has been started')
    [t.join() for t in list_of_thread]
    print('Threads is finish, Continue another line')
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    # make the Pool of workers
    pool = ThreadPool(4)
    # and return the results
    pool.map(sleep_function, range(5, 15))
    print("--- %s seconds ---" % (time.time() - start_time))
