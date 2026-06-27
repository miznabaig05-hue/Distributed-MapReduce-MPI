# generate_data.py
with open("dataset.txt", "w") as f:
    content = "apple banana orange grape mango strawberry blueberry " * 10000
    for i in range(50): # This creates a file with 500,000 words
        f.write(content + "\n")
print("Dataset created: dataset.txt")