import teFileHandler

passCount = 0
failCount = 0
totalCount = 0

def runTest(function, varible, negate=False):
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

#################################
## Set Variables for the tests ##
#################################
f1 = "tests\\teFileHandler\\file1.txt"
f2 = "tests\\teFileHandler\\dir1\\file2.txt"
f3 = "tests\\teFileHandler\\dir2\\file3.txt"
f4 = "tests\\teFileHandler\\dir2\\dir3\\file4.txt"

d1 = "tests\\teFileHandler\\dir1"
d2 = "tests\\teFileHandler\\dir2"
d3 = "tests\\teFileHandler\\dir2\\dir3"

###########################
## Create the test cases ##
###########################

print "Positive File Test"
runTest(teFileHandler.isFile, f1)
runTest(teFileHandler.isFile, f2)
runTest(teFileHandler.isFile, f3)
runTest(teFileHandler.isFile, f4)

print "Negative File Test"
runTest(teFileHandler.isFile, d1, True)
runTest(teFileHandler.isFile, d2, True)
runTest(teFileHandler.isFile, d3, True)

print "Positive Directory Test"
runTest(teFileHandler.isDirectory, d1)
runTest(teFileHandler.isDirectory, d2)
runTest(teFileHandler.isDirectory, d3)

print "Negative Directory Test"
runTest(teFileHandler.isDirectory, f1, True)
runTest(teFileHandler.isDirectory, f2, True)
runTest(teFileHandler.isDirectory, f3, True)

###################
## Final Results ##
###################

print totalCount, "tests."
print passCount, "passes."
print failCount, "failures."