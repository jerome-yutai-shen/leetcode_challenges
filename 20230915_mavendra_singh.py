# -*- coding: utf-8 -*-
"""
Created on Sep 15 10:53:23 2023

@author: Jerome Yutai Shen

"""
import multiprocessing

def calculate_sum(start, end, vector):
    partial_sum = sum(vector[start:end])
    return partial_sum

def parallel_sum(vector, num_processes):
    chunk_size = len(vector) // num_processes
    pool = multiprocessing.Pool(processes=num_processes)
    results = []

    for i in range(num_processes):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_processes - 1 else len(vector)
        results.append(pool.apply_async(calculate_sum, (start, end, vector)))

    pool.close()
    pool.join()

    total_sum = sum(result.get() for result in results)
    return total_sum


import threading

def calculate_sum2(start, end, vector):
    partial_sum = sum(vector[start:end])
    return partial_sum

def parallel_sum2(vector, num_threads):
    chunk_size = len(vector) // num_threads
    threads = []
    results = []

    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_threads - 1 else len(vector)
        thread = threading.Thread(target=lambda: results.append(calculate_sum(start, end, vector)))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    total_sum = sum(results)
    return total_sum

if __name__ == "__main__":
    vector = [i for i in range(1, 1000001)]  # Replace with your vector
    num_threads = 4  # Adjust based on your CPU cores
    result = parallel_sum2(vector, num_threads)
    print("Sum:", result)

    num_processes = 4  # Adjust based on your CPU cores
    result = parallel_sum(vector, num_processes)
    print("Sum:", result)


