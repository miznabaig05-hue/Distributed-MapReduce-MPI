from mpi4py import MPI
import time
import os
from mapper import map_chunk
from reducer import reduce_results

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# --- MASTER PROCESS ---
if rank == 0:
    print(f"--- [MASTER] Starting MapReduce System with {size} processes ---")
    
    # 1. READ DATASET FILE
    if not os.path.exists("dataset.txt"):
        print("Error: dataset.txt not found!")
        comm.Abort()

    with open("dataset.txt", "r") as f:
        all_lines = f.readlines()

    # 2. DATA PARTITIONING (Requirement: Distribute data)
    num_workers = size - 1
    if num_workers < 1:
        print("Error: Run with at least -n 2")
        comm.Abort()

    # Split the list of lines into chunks for each worker
    avg = len(all_lines) // num_workers
    chunks = []
    for i in range(num_workers):
        start = i * avg
        # The last worker gets the remaining lines
        end = (i + 1) * avg if i != num_workers - 1 else len(all_lines)
        # Join lines back into a single string for the worker
        chunks.append(" ".join(all_lines[start:end]))

    start_time = time.time()

    # 3. COMMUNICATION: Send chunks to workers
    for i in range(1, size):
        comm.send(chunks[i-1], dest=i)
        print(f"Master: Sent partition to Worker {i}")

    # 4. PARALLEL REDUCE: Collect and Merge
    final_word_counts = {}
    for i in range(1, size):
        worker_data = comm.recv(source=i)
        final_word_counts = reduce_results(final_word_counts, worker_data)
        print(f"Master: Received results from Worker {i}")

    end_time = time.time()

    # 5. OUTPUT RESULTS (Requirement: Produce correct outputs)
    print("\n" + "="*30)
    print("MAPREDUCE FINAL RESULTS")
    print("="*30)
    # Print the counts for the words we put in the file
    for word in ["apple", "banana", "orange", "mango"]:
        print(f"{word.capitalize()}: {final_word_counts.get(word, 0)}")
    
    print(f"\nExecution Time: {end_time - start_time:.4f} seconds")
    print("="*30)

# --- WORKER PROCESSES ---
else:
    # 1. Receive its specific partition
    my_data = comm.recv(source=0)
    
    # 2. Map Operation (Requirement: Parallel Map)
    my_results = map_chunk(my_data)
    
    # 3. Communication: Send back to Master
    comm.send(my_results, dest=0)