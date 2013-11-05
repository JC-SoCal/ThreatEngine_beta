import teFileHandler

passCount = 0
failCount = 0
totalCount = 0

def testIsDirectory(function, varible, negate):
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

print "Positive Directory Test"
testIsDirectory(teFileHandler.isDirectory, d1, False)
testIsDirectory(teFileHandler.isDirectory, d2, False)
testIsDirectory(teFileHandler.isDirectory, d3, False)
testIsDirectory(teFileHandler.isDirectory, d4, False)


print "Negative Directory Test"
testIsDirectory(teFileHandler.isDirectory, f1, True)
testIsDirectory(teFileHandler.isDirectory, f2, True)
testIsDirectory(teFileHandler.isDirectory, f3, True)
testIsDirectory(teFileHandler.isDirectory, f4, True)

###################
## Final Results ##
###################

print totalCount, "tests."
print passCount, "passes."
print failCount, "failures."