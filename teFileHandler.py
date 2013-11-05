import os
import fnmatch


def isFile(filepath):
  #check if file is from allowable type
  filetypes = ['.txt','.log','.csv','.pcap']

  for filetype in filetypes:
    if filepath.endswith(filetype):
      return True
  return False

def isDirectory(filepath):
  #check if filepath is is a directory
  if os.path.isdir(filepath):
    return True
  else:
    return False

def getFilesFromDirectory(filepath,recursive=False):
  #the output will be a tuple of true/false, and a list of the files
  files = []
  if isDirectory(filepath):
    if recursive:
      for root, dirnames, filenames in os.walk(filepath):
        for filename in filenames:
          if isFile(os.path.join(root,filename)):
            files.append(os.path.join(root,filename))
      return True, files
    else:
      for filename in os.listdir(filepath):
        if isFile(os.path.join(filepath,filename)):
          files.append(os.path.join(filepath,filename))
      return True, files
  else:
    return False, files