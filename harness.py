import teFileHandler
import tePcapFileParser
import teTextFileParser


testdata = "testdata\\harness_test"

#sort what the user gave us
sortedFiles = teFileHandler.getFilesSorted(testdata)

stats = teFileHandler.getStats(sortedFiles)
for entry in stats:
  print entry

#aggregate and dedupe

# build modules for intel gathering 

# thread them / throttle them



#what are my filters:
#ip
#domain name
#resolved ip # network connection required
#md5
#sha1