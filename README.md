# ⚡ Distributed MapReduce Framework (MPI)

This project is a custom-built **MapReduce Framework** designed to handle parallel word-count analysis on large datasets. Built using **Python** and **MPI (Message Passing Interface)**, it utilizes a Master-Worker architecture to demonstrate the power of distributed computing.

## 🤖 Why this matters for AI & UX
- **AI Infrastructure:** Training Large Language Models (LLMs) requires distributing data across hundreds of nodes. This project demonstrates my understanding of the core principles behind scaling AI.
- **System UX:** Parallel processing is the key to reducing latency. By optimizing the "backend" speed, we create a more seamless and responsive experience for the end-user.

---

## 🏗️ Master-Worker Architecture
- **Master Node:** Orchestrates the system, partitions the dataset, and assigns tasks.
- **Worker Nodes:** Execute the **Map** and **Reduce** logic in parallel, communicating results back to the Master.

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **Protocol:** MPI (Message Passing Interface)
- **Library:** `mpi4py`
- **Environment:** VS Code / Windows 11 (MS-MPI)

## 🚀 How to Run
1. **Generate the Dataset:**
   ```bash
   python generate_data.py
