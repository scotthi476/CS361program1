import os.path
import time
import random
from pathlib import Path
import sys
import subprocess

# UI takes user command
print("Please type star if you want to start star rating recipe search or enter 2 to quit \n")
input1 = input()
if (input1 == str("star")):
  file1 = open("callSearchMicroservice.txt", "r+")
  file1.write("star")
  file1.flush()
  file1.close()
  time.sleep(5)

  file1 = open("callSearchMicroservice.txt", "r+")
  data = file1.readline()
  if (data.find("star") != -1):
    #theproc = subprocess.Popen([sys.executable, "testRatingSearch.py"])
    theproc = subprocess.Popen([sys.executable, "ratingSearchServiceUI.py"])
    theproc.communicate()
  else:
    print("cannot find star")
  file1.close()


