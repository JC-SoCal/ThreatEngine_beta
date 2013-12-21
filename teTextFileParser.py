import socket
import re

# def f_IPv4(data):
#   #import socket
#   filterName = 'IP'
#   data = str(data)
#   try:
#     socket.inet_aton(data)
#   except:
#     pass
#   else:
#     if len((map(int, data.split('.')))) == 4:
#       return True, {filterName: data}
#   return False, {}
def f_IPv4(ip):
  #import socket
  try:
    socket.inet_aton(ip)
    return True
  except socket.error:
    return False

def f_NotRFC1918(ip):
  if f_IPv4(ip):
    try:
      octets = map(int, ip.split('.'))
    except:
      return False

    if octets[0] == 10: 
      return False
    elif octets[0] == 172 and octets[1] in range(16,32): 
      return False
    elif octets[0] == 192 and octets[1] == 168: 
      return False
    else: 
      return True
  else:
    return False
 
def f_Domain(name):
  #import re
  regex = "https?://\w+\.\w+" 
  #regex = "^[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}$"
  if re.match(regex, name):
    return True
  else:
    return False

def f_ValidatedDomain(name):
  #import socket
  try:
    if f_Domains(name):
      if socket.getaddrinfo(name, None):
        result = socket.getaddrinfo(name, None)
        #print result[0][4]
        return True
  except:
      return False

def f_MD5Hashes(data):
  #go back to regex if len(re.findall(r"([a-fA-F\d]{32})", data)) == 1 and len(data) == 32:
  filterName = 'MD5'
  if all(char.lower() in "0123456789abcdef" for char in data) and len(data) == 32:
    return True
  else:
    return False

def f_SHA1Hashes(data):
  filterName = 'SHA1'
  if all(char.lower() in "0123456789abcdef" for char in data) and len(data) == 40:
    return True
  else:
    return False

def splitText(filepath):
  data = set([])
  with open(filepath, 'rb') as f:
    content = f.readlines()
    for item in content:
      clean = filter(None, re.split("[\s,]", item))
      for item in clean:
        data.add(item)
  return data

def filterData(data,filters=[]):
  filteredData = set([])
  for item in data:
    for f in filters:
      if f(item):
        filteredData.add(item)
  return filteredData

def parseText(filepath):
  data = splitText(filepath)
  ips = filterData(data,filters=[f_IPv4])
  domains = filterData(data,filters=[f_Domain])
  md5hashes = filterData(data,filters=[f_MD5Hashes])
  sha1hashes = filterData(data,filters=[f_SHA1Hashes])
  result = {}
  result['filename'] = [filepath]
  result['ips'] = list(ips)
  result['domains'] = list(domains)
  result['md5hashes'] = list(md5hashes)
  result['sha1hashes'] = list(sha1hashes)
  return True,result