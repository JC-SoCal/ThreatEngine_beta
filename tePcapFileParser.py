import dpkt
import socket
import binascii
import sys
import re

####################
## FILE FUNCTIONS ##
####################
def readFile(filename):
  try:
    f = open(filename, 'rb')
    return f
  except:
    print "ERROR: Could Not Open:", filename
    return False
  
def closeFile(handle):
  try:
    return handle.close()
  except:
    return False

####################
## PCAP FUNCTIONS ##
####################
def openPCAP(fileHandle):
  #import dpkt
  return dpkt.pcap.Reader(fileHandle)
 
def carveData(pcap,carvers=[]):
  #import dpkt
  data = set([])
  for ts, buff in pcap:
    try:
      eth = dpkt.ethernet.Ethernet(buff)
      for carver in carvers:
        for item in carver(eth):
          data.add(item)
    except: 
      pass

  return data

def filterData(data,filters=[]):
  filteredData = set([])
  for item in data:
    for f in filters:
      if f(item):
        filteredData.add(item)
  return filteredData

###############
## CARVERS ##
###############
def c_IPv4(eth):  
  #import socket
  IPs = []  
  try:
    ip = eth.data
    try:
      IPs.append(socket.inet_ntoa(ip.src))
    except: pass
    try:
      IPs.append(socket.inet_ntoa(ip.dst))
    except: pass
  except: pass
  return IPs

def c_Domain(eth):
  #import dpkt
  data = []
  try:
    ip = eth.data
    if eth.type == 2048:
      if ip.p == 17:
        udp = ip.data
        if udp.sport == 53 or udp.dport == 53: 
          dns = dpkt.dns.DNS(udp.data)
          if dns.qr == dpkt.dns.DNS_R: 
            if dns.opcode == dpkt.dns.DNS_QUERY: 
              if dns.rcode == dpkt.dns.DNS_RCODE_NOERR: 
                if len(dns.an) > 0: 
                  for answer in dns.an:
                    data.append(answer.name)
                    if answer.type == 5: data.append(answer.cname)
                    elif answer.type == 1: data.append(socket.inet_ntoa(answer.rdata))
                    elif answer.type == 12: data.append(answer.ptrname)
  except: 
    pass
  return data

#############
## FILTERS ##
#############
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

def f_IPv4(ip):
  #import socket
  try:
    socket.inet_aton(ip)
    return True
  except socket.error:
    return False

def f_Domain(name):
  #import re
  regex = "^[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}$"
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

def parsePCAP(filepath):
  h = readFile(filepath)
  pcap = openPCAP(h)
  data = carveData(pcap,[c_IPv4,c_Domain])
  result = []
  ips = filterData(data,filters=[f_IPv4])
  domains = filterData(data,filters=[f_Domain])
  result.append({'ips':list(ips)})
  result.append({'domains':list(domains)})
  closeFile(h)
  return True,result