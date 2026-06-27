# mapper.py
def map_chunk(text):
    """Processes a piece of text and returns word counts."""
    counts = {}
    words = text.split()
    for word in words:
        clean_word = word.lower().strip(".,!?:;")
        if clean_word:
            counts[clean_word] = counts.get(clean_word, 0) + 1
    return counts