# BXACK
ICT 2202 (Digital Forensics) Project 

Version: 1.0

This tool is created to assist Network Forensics Analyst to extract and analyze raw core dump files directly from Cisco Network Devices. The information retrieved will be stored in pdf files to be used as digital evidence, preserve chain of custody, or for further analysis.


## Detailed Manual Guide
Link: https://github.com/benjaminkoh1994/BXACK/blob/main/Manual.pdf


## Video Demostration
Youtube Link: https://www.youtube.com/watch?v=G_T4pyE9vrs


## Documentation on Project Package 
BXACK Project consists of three module namely:

* program.py
```
program.py is the main file which utilizes the subsequent python files (extract.py, ssh.py) to run the program. This file instantiates the imported classes and defines the flow of BXACK.
```
* extract.py
```
This file contains 2 classes (EXTRACTCMD, EXTRACTSECT) that are associated to Option B of BXACK program, to analyze cisco forensic evidence. These 2 classes extract and clean the data before displaying it as outputs for analysis.
```
* ssh.py
```
This file contains 1 class that is shared among Option A and Option C of the BXACK program. It launches an SSH connection using Paramiko library for forensic evidence acquisition before cleaning the data and displaying it as output for analysis.
```

## Getting Started

These instructions will get you a copy of the project up and running on your local machine. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
* Using [pip](https://pip.pypa.io/en/stable/) install:
* PyFPDF - Generate PDF files
```
pip install fpdf
```
* difflib - Check differences between files
```
pip install difflib
```
* datetime - Control flow of program
```
pip install difflib
```
* paramiko - Enable SSH connection
```
pip install difflib
```



