Here are my answers: 

Exercise 1: Threaded Prime Number Checker
import threading

# Helper function to test primality
def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Worker function for each thread
def prime_worker(start, end, result, lock):
    local_primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            local_primes.append(num)
    # Lock ensures only one thread updates shared list at a time
    with lock:
        result.extend(local_primes)

# Main threaded function
def threaded_prime_range(start: int, end: int, num_threads: int = 4):
    """Find primes in a given range using multiple threads."""
    if start > end:
        start, end = end, start

    result = []
    lock = threading.Lock()
    threads = []

    # Divide the range evenly among threads
    total_numbers = end - start + 1
    chunk = total_numbers // num_threads
    remainder = total_numbers % num_threads

    cur = start
    for i in range(num_threads):
        size = chunk + (1 if i < remainder else 0)
        thread_start = cur
        thread_end = cur + size - 1
        t = threading.Thread(target=prime_worker, args=(thread_start, thread_end, result, lock))
        threads.append(t)
        t.start()
        cur = thread_end + 1

    for t in threads:
        t.join()

    return sorted(result)


# Example usage
if __name__ == "__main__":
    primes = threaded_prime_range(1, 100, num_threads=4)
    print("Primes between 1 and 100:", primes)

__________________________________________________________________

Exercise 2: Threaded File Processing (Word Count)
import threading
import queue
import collections
import re

def threaded_word_count(file_path: str, num_workers: int = 4, lines_per_batch: int = 200):
    """
    Count word occurrences in a text file using threads.
    Each thread processes a batch of lines.
    """
    q = queue.Queue(maxsize=num_workers * 2)
    counters = [collections.Counter() for _ in range(num_workers)]
    STOP = object()  # sentinel value

    # Producer: reads file and puts batches of lines into queue
    def producer():
        with open(file_path, "r", encoding="utf-8") as f:
            batch = []
            for line in f:
                batch.append(line)
                if len(batch) >= lines_per_batch:
                    q.put(batch)
                    batch = []
            if batch:
                q.put(batch)
        for _ in range(num_workers):
            q.put(STOP)

    # Worker: processes lines and counts words
    def worker(idx):
        local = counters[idx]
        while True:
            batch = q.get()
            try:
                if batch is STOP:
                    break
                for line in batch:
                    for word in re.findall(r"\b\w+\b", line.lower()):
                        local[word] += 1
            finally:
                q.task_done()

    # Start workers
    threads = []
    for i in range(num_workers):
        t = threading.Thread(target=worker, args=(i,), daemon=True)
        t.start()
        threads.append(t)

    # Run producer in main thread
    producer()

    # Wait until all work is done
    q.join()

    # Merge results
    final_counter = collections.Counter()
    for c in counters:
        final_counter.update(c)

    return final_counter


# Example usage
if __name__ == "__main__":
    # Create a sample text file
    sample_file = "sample_text.txt"
    with open(sample_file, "w", encoding="utf-8") as f:
        f.write("Concurrency in Python is powerful.\n")
        f.write("Threads can be used for I/O-bound tasks.\n")
        f.write("Python threads share memory space.\n")

    result = threaded_word_count(sample_file, num_workers=3, lines_per_batch=2)
    print("Word counts:", result.most_common())
