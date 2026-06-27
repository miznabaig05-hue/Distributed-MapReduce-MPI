===========================================================
PROJECT: Distributed MapReduce Framework using MPI
COURSE: Parallel and Distributed Computing
BATCH: CS-SP-23
===========================================================

1. PROJECT OVERVIEW
-------------------
This project implements a modular MapReduce framework using Python 
and MPI (Message Passing Interface). It follows a Master-Worker 
architecture to perform parallel word-count analysis on a large 
dataset.

2. PREREQUISITES (SYSTEM REQUIREMENTS)
--------------------------------------
To run this project on Windows 11, ensure the following are installed:
- Python 3.10 or higher.
- Microsoft MPI (MS-MPI v10+): 
  Download: msmpisetup.exe and msmpisdk.msi
- mpi4py library:
  Install via: pip install mpi4py

3. FILE STRUCTURE
-----------------
- main.py           : The orchestration engine (Master-Worker logic).
- mapper.py         : Contains logic for the Map phase (word counting).
- reducer.py        : Contains logic for the Reduce phase (merging results).
- generate_data.py  : Script to generate the test dataset.
- dataset.txt       : The input file (created by generate_data.py).
- README.txt        : Execution instructions (this file).
- Report_Design_Doc.pdf : Detailed project report and analysis.

4. EXECUTION STEPS
------------------
Follow these steps in order using the Terminal (Command Prompt/PowerShell):

Step 1: Generate the Dataset
Run the following command to create the 100,000-line dataset:
> python generate_data.py

Step 2: Run the MapReduce System
Use the MPI executor to run the system with multiple processes.
To run with 4 processes (1 Master, 3 Workers):
> mpiexec -n 4 python main.py

To test scalability, you can change the number of processes:
> mpiexec -n 2 python main.py
> mpiexec -n 8 python main.py

5. NOTES
--------
- Ensure all .py files are in the same folder.
- Ensure dataset.txt is generated before running main.py.
- If an "ImportError" occurs, check that your VS Code Python 
  Interpreter matches the environment where mpi4py was installed.

===========================================================
Submitted by: Mizna Baig, Binshah Joseph
===========================================================