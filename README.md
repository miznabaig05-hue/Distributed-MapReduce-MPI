# ⚡ Distributed MapReduce Framework (Python + MPI)

This project implements a modular **MapReduce framework** using a **Master-Worker architecture**. It is designed to perform parallel word-count analysis on large datasets, showcasing the power of **Distributed Systems** and **Parallel Computing**.

---

## 🧠 Connection to AI & Data Science
Before AI models can be trained, massive amounts of data must be processed. **MapReduce** is the foundational logic used by industry giants (like Google and Apache Spark) to handle "Big Data." Understanding this infrastructure is key to scaling AI-driven applications.

## 🚀 Key Features
- **Master-Worker Architecture:** Efficiently orchestrates tasks across multiple processing nodes.
- **Parallel Processing:** Splits large datasets to be processed simultaneously, significantly reducing execution time.
- **Scalability:** Tested across multiple processes (2, 4, and 8) to analyze performance gains.
- **Modular Design:** Separate logic for Mapping, Reducing, and Orchestration.

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **Protocol:** MPI (Message Passing Interface)
- **Libraries:** `mpi4py`
- **Environment:** VS Code / Windows 11 (MS-MPI)

## 📋 File Structure
- `main.py`: The orchestration engine (Master-Worker logic).
- `mapper.py`: Logic for the Map phase (word counting).
- `reducer.py`: Logic for the Reduce phase (merging results).
- `generate_data.py`: Script to generate a 100,000-line test dataset.
- `Report_Design_Doc.pdf`: **Detailed technical analysis and performance report.**

## ⚙️ How to Run
1. **Generate the Dataset:**
   ```bash
   python generate_data.py
2. **Run the MapReduce System (e.g., with 4 processes):**
   ```bash
   mpiexec -n 4 python main.py
