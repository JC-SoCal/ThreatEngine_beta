import teFileHandler

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


#################################
## Set Variables for the tests ##
#################################
f1 = "tests\\teFileHandler\\file1.txt"
f2 = "tests\\teFileHandler\\dir1\\file2.txt"
f3 = "tests\\teFileHandler\\dir2\\file3.txt"
f4 = "tests\\teFileHandler\\dir2\\dir3\\file4.txt"

d1 = "tests\\teFileHandler"
d2 = "tests\\teFileHandler\\dir1"
d3 = "tests\\teFileHandler\\dir2"
d4 = "tests\\teFileHandler\\dir2\\dir3"

###########################
## Create the test cases ##
###########################

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

###################
## Final Results ##
###################

print totalCount, "tests."
print passCount, "passes."
print failCount, "failures."