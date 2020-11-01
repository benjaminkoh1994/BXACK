# BXACK
ICT 2202 (Digital Forensics) Project 

Version: 1.0

This tool is created to assist Network Forensics Analyst to extract and analyze raw core dump files directly from Cisco Network Devices. The information retrieved will be stored in pdf files to be used as digital evidence, preserve chain of custody, or for further analysis.


## Detailed Manual Guide
Link: https://github.com/benjaminkoh1994/BXACK/blob/main/Manual.pdf


## Video Demonstration
Youtube Link: https://www.youtube.com/watch?v=G_T4pyE9vrs


## Documentation on Project Package 
BXACK Project consists of three module namely:

* program.py

program.py is the main file which utilizes the subsequent python files (extract.py, ssh.py) to run the program. This file instantiates the imported classes and defines the flow of BXACK.

* extract.py

This file contains 2 classes (EXTRACTCMD, EXTRACTSECT) that are associated to Option B of BXACK program, to analyze cisco forensic evidence. These 2 classes extract and clean the data before displaying it as outputs for analysis.

* ssh.py

This file contains 1 class that is shared among Option A and Option C of the BXACK program. It launches an SSH connection using Paramiko library for forensic evidence acquisition before cleaning the data and displaying it as output for analysis.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
* Using [pip](https://pip.pypa.io/en/stable/) install:
* **These are the main dependencies**
```
pip install fpdf
```
```
pip install difflib
```
```
pip install datetime
```
```
pip install paramiko
```

## Running the tests

Using cmd, Run program.py
```
python program.py
```
![WhatsApp Image 2020-11-01 at 16 23 44](https://user-images.githubusercontent.com/57383960/97798485-78431600-1c61-11eb-8fed-6fb289ebb908.jpeg)

## Built With

* [Python3](https://www.python.org/downloads/) - Language used
* [PyFPDF](https://pypi.org/project/PyFDP/) - Generate PDF files
* [difflib](https://pypi.org/project/cdifflib/) - Check differences between files
* [datetime](https://pypi.org/project/DateTime/) - Control flow of program
* [paramiko](https://pypi.org/project/paramiko/) - Enable SSH connection

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Koh Jie Ming, Benjamin**
* **Ee Xian Hui**
* **Koh Kai Quan**
* **Ong Chang Hong**
* **Chua An Rong Aaron**

See also the list of [contributors](CONTRIBUTING.md) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
