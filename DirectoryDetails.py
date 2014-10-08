#!/usr/bin/python

import sys
import os, time
from stat import *
from os import *

# Print information about the directory components recursively
def directory_info(dir_path):
  # Check for the existence of directory
  if not (os.path.isdir(dir_path)):
    print ("Directory %s does not exist" %(dir_path))
    return

  # Get the directory's list of subdirectories in dirnames and filelists 
  # in filenames
  for (dirpath, dirnames, filenames) in walk(dir_path):
    break

  # Print directory name
  print ("Directory <" + dir_path + ">")
  sorted_list = []


  for file in filenames:
    # Fetch file information
    try:
      st = os.stat(os.path.join(dirpath, file))
    except IOError:
      print ("File not found")
    else:
      sorted_list.append([st[ST_SIZE], time.asctime(time.localtime(st[ST_MTIME])), file])

  # Print the file information in the descending order by size
  for entry in sorted(sorted_list, reverse=True):
    print ("%10d %s %s" % (entry[0], entry[1], entry[2]))
  print ("\n")

  # Call the function recursively for the subdirectories
  for dir in dirnames:
    directory_info(os.path.join(dirpath, dir))

# Get the infomation for the directory given through command line
directory_info(".")
