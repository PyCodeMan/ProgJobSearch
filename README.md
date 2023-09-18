# ProgJobSearch
An automated system to help programmers find orders on freelance burses, aviable on Linux shell, Termux and Python interpreters

# For whom?
For Python programmers who want to simplify and automate the order search procedure

# How will this help?
The system reads and outputs texts from four freelance burses to the terminal at once, which allows you not to view everything in the browser yourself, but simply press a few buttons.

# Download instructions

Download on Linux:
1. sudo su (to avoid having to confirm each subsequent action with a password)
2. apt update && apt upgrade -y
3. apt install python3
4. apt install pip
4.1. If the fourth command did not work and send you to PEP668 - apt install python3-requests && apt install python3-lxml && apt install python3-bs4 -y
4.2. exit
4.3. git clone https://github.com/PyCodeMan/ProgJobSearch/
4.4. The program is ready to launch, go to the launch instructions
5. exit
6. git clone https://github.com/PyCodeMan/ProgJobSearch/
7. cd ProgJobSearch
8. pip install -r requirements.txt (if did not work - try 4.1.)
9. The program is ready to launch, go to the launch instructions

Download on Termux:
1. pkg update && pkg upgrade -y
2. proot distro login "your distribution name" (without "")
3. apt update && apt upgrade -y
4. apt install python3
5. apt install pip
5.1. If the fivth command did not work and send you to PEP668 - apt install python3-requests && apt install python3-lxml && apt install python3-bs4 -y
5.2. exit
5.3. git clone https://github.com/PyCodeMan/ProgJobSearch/
5.4. The program is ready to launch, go to the launch instructions
6. exit
7. git clone https://github.com/PyCodeMan/ProgJobSearch/
8. cd ProgJobSearch
9. pip install -r requirements.txt (if did not work - try 5.1.)
10. The program is ready to launch, go to the launch instructions

# Launch instructions

1. cd ProgJobSearch
2. python ProgJobSearch.py (if did not work - python3 ProgJobSearch.py)
3. Enjoy

# How to use on Windows or Android?
If you have a Python interpreter on Android or Windows, just copy and paste the program code there. However, do not forget about installing the libraries necessary for the program to work - bs4, time and requests.

Please, if you have any issues - let me know, I'll help you.
