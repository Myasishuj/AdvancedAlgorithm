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
        numbers.append(random.randint(0, 10000))
    # End timer and calculate duration
    end = time.perf_counter_ns()
    duration = end - start
        print(f"{threading.current_thread().name} ran for {duration} ns ({duration / 1e6:.3f} ms)")

def generate_nums_no_thread():
    numbers = []
    for i in range(100):
        numbers.append(random.randint(0, 10000))

def main():
    round_num = 10
    threading_time=[]
    normal_time=[]
    total_time=0
    print("Starting 10 rounds of random number generation with 3 threads each.")
    print("-" * 60)

    for i in range(round_num):
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
        end_all = time.perf_counter_ns()

        threading_time.append(end_all-start_all)
    for i in range(round_num):
        total_time+=threading_time[i]
        print(
            f"Round {i+1}: Time taken = {threading_time[i]} ns ({threading_time[i] / 1e6:.3f} ms)")

    print("-" * 60)
    print(f"Average total runtime over {round_num} "
          f"rounds: {total_time/round_num:.0f} ns ({total_time/round_num / 1e6:.3f} ms)")
    print("-" * 60)


    total_time=0
    print("Starting 3 rounds of random number generation without threading.")
    for i in range(round_num):
        start_all = time.perf_counter_ns()

        generate_nums_no_thread()
        generate_nums_no_thread()
        generate_nums_no_thread()

        end_all = time.perf_counter_ns()

        normal_time.append(end_all-start_all)

        total_time += normal_time[i]

    for i in range(round_num):
        print(f"Round {i + 1}: Time taken = {normal_time[i]} ns ({normal_time[i] / 1e6:.3f} ms)")
    print("-" * 60)
    print(f"Average total runtime over {round_num} "
          f"rounds: {total_time/3:.0f} ns ({total_time/3 / 1e6:.3f} ms)")
    print("-" * 60)

   # Print Round-by-Round Performance Comparison
    print("\nRound-by-Round Performance Comparison:")
    print(f"| {'Round':^5} | {'Multithreading Time (ns)':^25} | {'Non-Multithreading Time (ns)':^28} | {'Difference (ns)':^18} |")
    print("|" + "-"*7 + "|" + "-"*27 + "|" + "-"*30 + "|" + "-"*20 + "|")

    differences = []
    for i in range(round_num):
        diff = threading_time[i] - normal_time[i]
        differences.append(diff)
        print(f"| {i+1:^5} | {threading_time[i]:^25} | {normal_time[i]:^28} | {diff:^18} |")

    # Summary of Results
    total_thread_time = sum(threading_time)
    total_non_thread_time = sum(normal_time)
    total_diff = total_thread_time - total_non_thread_time

    print("\nSummary of Results:")
    print(f"| {'Metric':^12} | {'Multithreading':^15} | {'Non-Multithreading':^20} | {'Difference (ns)':^18} |")
    print("|" + "-"*14 + "|" + "-"*17 + "|" + "-"*22 + "|" + "-"*20 + "|")
    print(f"| {'Total Time': ^11}  | {total_thread_time:^15} | {total_non_thread_time:^20} | {total_diff:^18} |")
    print(f"| {'Average Time':^10} | {total_thread_time/round_num:^15.1f} | {total_non_thread_time/round_num:^20.1f} | {total_diff/round_num:^18.1f} |")
    
if __name__=="__main__":
    main()
