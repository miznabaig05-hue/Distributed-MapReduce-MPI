# reducer.py
def reduce_results(master_dict, worker_dict):
    """Merges a worker's word counts into the main results dictionary."""
    for word, count in worker_dict.items():
        master_dict[word] = master_dict.get(word, 0) + count
    return master_dict