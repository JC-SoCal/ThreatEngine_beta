import os
import fnmatch

filetypes = ['*.txt','*.log','*.csv','*.pcap']

def isFile(filepath):
  #check if the filepath is just a single filepath
  #if yes, return true, not false
  return os.path.isfile(filepath)

def isDirectory(filepath):
  #check if filepath is isDirectory
  #if yes return true, else false
  return os.path.isdir(filepath)

def getFilesFromDirectory(filepath,recursive=False):
  if isDirectory(filepath):
    files = []
    if recursive:
      for root, dirnames, filenames in os.walk(filepath):
        for filetype in filetypes:
          for filename in fnmatch.filter(filenames, filetype):
            files.append(os.path.join(root,filename))
      return True, files
    else:
      for item in os.listdir(filepath):
        if isFile(os.path.join(filepath,item)):
          files.append(os.path.join(filepath,item))
      return True, files
  else:
    return False, files