import concurrent.futures
import random
import threading
import time

def sleep_and_return_duration():
    """Sleeps for a random amount of time and returns the sleep duration."""
    sleep_duration = random.random() * 10
    time.sleep(sleep_duration)
    print(f"Thread {threading.get_ident()} slept for {sleep_duration:.2f} seconds")
    return sleep_duration

def run_parallel_tasks(num_tasks):
    """Runs the sleep_and_return_duration function in parallel using ThreadPoolExecutor."""
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks to the executor
        futures = [executor.submit(sleep_and_return_duration) for _ in range(num_tasks)]

        # Wait for all tasks to complete
        workload_times = [future.result() for future in concurrent.futures.as_completed(futures)]

    total_workload_time = sum(workload_times)
    max_workload_time = max(workload_times)
    return total_workload_time, max_workload_time

if __name__ == "__main__":
    start_time = time.time()
    total_workload_time, max_workload_time = run_parallel_tasks(20)
    elapsed_time = time.time() - start_time

    print(f"Total workload time: {total_workload_time:.2f} seconds")
    print(f"Max workload time: {max_workload_time:.2f} seconds")
    print(f"Elapsed time: {elapsed_time:.2f} seconds")