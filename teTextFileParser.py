import socket
import re

def f_IP(data):
  #import socket
  filterName = 'IP'
  data = str(data)
  try:
    socket.inet_aton(data)
  except:
    pass
  else:
    if len((map(int, data.split('.')))) == 4:
      return True, {filterName: data}
  return False, {}
 
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

def f_hashes(data):
  #go back to regex if len(re.findall(r"([a-fA-F\d]{32})", data)) == 1 and len(data) == 32:
  filterName = 'MD5'
  if all(char.lower() in "0123456789abcdef" for char in data) and len(data) == 32:
    return True, {filterName: data}

  filterName = 'SHA1'
  if all(char.lower() in "0123456789abcdef" for char in data) and len(data) == 40:
    return True, {filterName: data} 

  return False, {}



# print f_IP('192.168.0.1')
# print f_IP('192.168.0.314')
# print f_IP('192.168.0')

# print f_hashes('900e3f2dd4efc9892793222d7a1cee4a')
# print f_hashes('AC905DD4AB2038E5F7EABEAE792AC41B')
# print f_hashes('900e3f2dd4efc9892793222d7a1cee4a900e3f2dd4efc9892793222d7a1cee4a')
# print f_hashes('trrololol')

# print f_hashes('d058b05200b93b27ef3e834b59bab5b478f4e9d5')
# print f_hashes('D058B05200B93B27EF3E834B59BAB5B478F4E9D5')
# print f_hashes('d058b05200b93b27ef3e834b59bab5b478f4e9d5d058b05200b93b27ef3e834b59bab5b478f4e9d5')
# print f_hashes('trrololol')

print f_Domain('http://')