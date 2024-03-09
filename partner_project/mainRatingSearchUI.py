import os.path
import time
import random
from pathlib import Path
import sys
import subprocess

# UI takes user command
print("Please type rating if you want to start star rating recipe search or enter 2 to quit \n")
input1 = input()
if (input1 == str("rating")):
  file1 = open("callSearchMicroservice.txt", "r+")
  file1.write("rating")
  file1.flush()
  file1.close()
  time.sleep(1)

  file1 = open("callSearchMicroservice.txt", "r+")
  data = file1.readline()
  if (data.find("rating") != -1):
    theproc = subprocess.Popen([sys.executable, "ratingSearchServiceUI.py"])
    theproc.communicate()
  else:
    print("cannot find rating")
  time.sleep(5)
  file1.seek(0)
  file1.truncate()
  file1.close()



