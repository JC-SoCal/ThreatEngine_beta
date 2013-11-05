from Code.ThreatEnginebeta import teFileHandler

passCount = 0
failCount = 0
totalCount = 0

def runIsTest(function, varible, negate=False):
	global passCount
	global failCount
	global totalCount

	totalCount += 1
	if negate:
		if function(varible):
			print "FAIL:",str(varible), "in",str(function.__name__)
			failCount += 1
		else:
			print "PASS"
			passCount += 1
	else:
		if function(varible):
			print "PASS"
			passCount += 1
		else:
			print "FAIL:",str(varible), "in",str(function.__name__)
			failCount += 1

def runGetFilesTest(function, varible, negate=False):
	pass

#################################
## Set Variables for the tests ##
#################################
f1 = "testdata\\teFileHandler\\file1.txt"
f2 = "testdata\\teFileHandler\\dir1\\file2.txt"
f3 = "testdata\\teFileHandler\\dir2\\file3.txt"
f4 = "testdata\\teFileHandler\\dir2\\dir3\\file4.txt"

d1 = "testdata\\teFileHandler"
d2 = "testdata\\teFileHandler\\dir1"
d3 = "testdata\\teFileHandler\\dir2"
d4 = "testdata\\teFileHandler\\dir2\\dir3"

###########################
## Create the test cases ##
###########################

print "Positive File Test"
runIsTest(teFileHandler.isFile, f1)
runIsTest(teFileHandler.isFile, f2)
runIsTest(teFileHandler.isFile, f3)
runIsTest(teFileHandler.isFile, f4)

print "Negative File Test"
runIsTest(teFileHandler.isFile, d1, True)
runIsTest(teFileHandler.isFile, d2, True)
runIsTest(teFileHandler.isFile, d3, True)
runIsTest(teFileHandler.isFile, d4, True)

print "Positive Directory Test"
runIsTest(teFileHandler.isDirectory, d1)
runIsTest(teFileHandler.isDirectory, d2)
runIsTest(teFileHandler.isDirectory, d3)
runIsTest(teFileHandler.isDirectory, d4)


print "Negative Directory Test"
runIsTest(teFileHandler.isDirectory, f1, True)
runIsTest(teFileHandler.isDirectory, f2, True)
runIsTest(teFileHandler.isDirectory, f3, True)
runIsTest(teFileHandler.isDirectory, f4, True)

print teFileHandler.getFilesFromDirectory(d1,True)
print teFileHandler.getFilesFromDirectory(d2,True)
print teFileHandler.getFilesFromDirectory(d3,True)
print teFileHandler.getFilesFromDirectory(d4,True)

print teFileHandler.getFilesFromDirectory(d1)
print teFileHandler.getFilesFromDirectory(d2)
print teFileHandler.getFilesFromDirectory(d3)
print teFileHandler.getFilesFromDirectory(d4)

###################
## Final Results ##
###################

print totalCount, "tests."
print passCount, "passes."
print failCount, "failures."