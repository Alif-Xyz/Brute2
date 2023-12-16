import os, sys
os.system("git pull")
try:
    __import__("BRUTE2").BRUTE2()
except Exception as e:
    exit(str(e))
