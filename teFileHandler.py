import os
import fnmatch
import struct
import mimetypes
import teTextFileParser
import tePcapFileParser


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

def isPcapFile(filepath):
  #determine if the file is a pcap
  pcapSig = '\xd4\xc3\xb2\xa1'
  with open(filepath, 'rb') as f:
    bytes = f.read(4)  
    fileSig = struct.unpack("4s", bytes)[0]
  if fileSig == pcapSig:
    return True
  else:
    return False

def isTextFile(filepath):
  #determine if the file is a pcap
  mime = mimetypes.guess_type(filepath)
  if 'text/plain' == mime[0]:
    return True
  else:
    return False

def sortFilesByType(files):
  #sorts files by their type, either text or pcap
  textFiles = []
  pcapFiles = []
  for f in files:
    if isTextFile(f):
      textFiles.append(f)
    elif isPcapFile(f):
      pcapFiles.append(f)
  return {'text':textFiles, 'pcap':pcapFiles}

def getFilesSorted(filepath):
  #determine what the user gave us, a file or directory?
  if isDirectory(filepath):
    status,files = getFilesFromDirectory(filepath)
  elif isFile(filepath):
    files = [filepath]
  return sortFilesByType(files)

def getStats(sortedFiles):
  stats = [] 
  for f in sortedFiles['pcap']:
    status, data = tePcapFileParser.parsePCAP(f)
    info = {}
    info['filename'] = data['filename']
    for name in data:
      if name != 'filename':
        info[name] = len(data[name])
    stats.append(info)
    # print data

  for f in sortedFiles['text']:
    status, data = teTextFileParser.parseText(f)
    info = {}
    info['filename'] = data['filename'][0]
    for name in data:
      if name != 'filename':
        info[name] = len(data[name])
    stats.append(info)
  return stats    