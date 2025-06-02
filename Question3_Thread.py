import threading
import time
import random

import threading
import time
import random


def generate_nums():
    # Start timer
    start = time.perf_counter_ns()
    print(f"{threading.current_thread().name} started.")

    numbers = []
    for i in range(100):
        # Action
        numbers.append(random.randint(0, 10000))
    # End timer and calculate duration
    end = time.perf_counter_ns()
    duration = end - start
    print(f"{threading.current_thread().name} ran for {duration} ns ({duration / 1e6:.3f} ms)")


def main():
    # Assign thread objects(T1,T2,T3) with a function and a name
    t1 = threading.Thread(target=generate_nums, name="Thread 1")
    t2 = threading.Thread(target=generate_nums, name="Thread 2")
    t3 = threading.Thread(target=generate_nums, name="Thread 3")

    start_all = time.perf_counter_ns()
    # Start running threads
    t1.start()
    t2.start()
    t3.start()

    # Wait for threads to finish
    t1.join()
    t2.join()
    t3.join()

    # End timer and calculate duration
    # Total runtime may include Overhead from python interperter, Waiting time from join() and context switching for threads
    end_all = time.perf_counter_ns()
    print(f"\nTotal runtime: {end_all - start_all} ns ({(end_all - start_all) / 1e6:.3f} ms)")
if __name__=="__main__":
    main()