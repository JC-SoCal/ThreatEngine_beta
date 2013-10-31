import re
import struct

def textParser(filepath):
  data = set([])
  with open(filepath, 'rb') as f:
    content = f.readlines()
    for item in content:
      clean = filter(None, re.split("[\s,]", item))
      for item in clean:
        data.add(item)
  return data

def isPcapFile(filepath):
  pcapSig = '\xd4\xc3\xb2\xa1'
  with open(filepath, 'rb') as f:
    bytes = f.read(4)  
    fileSig = struct.unpack("4s", bytes)[0]
  if fileSig == pcapSig:
    return True
  else:
    return False

def pcapParser(filepath):
  if not isPcapFile(filepath):
    return False
  #do PCAP stuff
  return True

