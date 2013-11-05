import teFileHandler

passCount = 0
failCount = 0
totalCount = 0
def testGetFilesFromDirectory(function, varible, expected, recursive, negate):
	global passCount
	global failCount
	global totalCount

	totalCount += 1
	if negate:
		status,data = function(varible,recursive)
		if status:
			if data == expected:
				print "FAIL:",str(varible), "in",str(function.__name__)
				failCount += 1
			else:
				print "PASS"
				passCount += 1
		else:
			print "PASS"
			passCount += 1
	else:
		status,data = function(varible,recursive)
		if status:
			if data == expected:
				print "PASS"
				passCount += 1
			else:
				print "FAIL:",str(varible), "in",str(function.__name__)
				failCount += 1
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
print "Get files from directory, non-recursive"
expected = ['testdata\\teFileHandler\\file1.txt']
testGetFilesFromDirectory(teFileHandler.getFilesFromDirectory, d1, expected, False, False)
expected = ['testdata\\teFileHandler\\dir1\\file2.txt']
testGetFilesFromDirectory(teFileHandler.getFilesFromDirectory, d2, expected, False, False)
expected = ['testdata\\teFileHandler\\dir2\\file3.txt']
testGetFilesFromDirectory(teFileHandler.getFilesFromDirectory, d3, expected, False, False)
expected = ['testdata\\teFileHandler\\dir2\\dir3\\file4.txt']
testGetFilesFromDirectory(teFileHandler.getFilesFromDirectory, d4, expected, False, False)

print "Get files from directory, recursive"
expected = ['testdata\\teFileHandler\\file1.txt', 'testdata\\teFileHandler\\dir1\\file2.txt', 'testdata\\teFileHandler\\dir2\\file3.txt', 'testdata\\teFileHandler\\dir2\\dir3\\file4.txt']
testGetFilesFromDirectory(teFileHandler.getFilesFromDirectory, d1, expected, True, False)
expected = ['testdata\\teFileHandler\\dir1\\file2.txt']
testGetFilesFromDirectory(teFileHandler.getFilesFromDirectory, d2, expected, True, False)
expected = ['testdata\\teFileHandler\\dir2\\file3.txt', 'testdata\\teFileHandler\\dir2\\dir3\\file4.txt']
testGetFilesFromDirectory(teFileHandler.getFilesFromDirectory, d3, expected, True, False)
expected = ['testdata\\teFileHandler\\dir2\\dir3\\file4.txt']
testGetFilesFromDirectory(teFileHandler.getFilesFromDirectory, d4, expected, True, False)

print "Negative Get files from directory, non-recursive"
expected = []
testGetFilesFromDirectory(teFileHandler.getFilesFromDirectory, f1, expected, False, True)
expected = []
testGetFilesFromDirectory(teFileHandler.getFilesFromDirectory, f2, expected, False, True)
expected = []
testGetFilesFromDirectory(teFileHandler.getFilesFromDirectory, f3, expected, False, True)
expected = []
testGetFilesFromDirectory(teFileHandler.getFilesFromDirectory, f4, expected, False, True)

print "Negative Get files from directory, recursive"
expected = []
testGetFilesFromDirectory(teFileHandler.getFilesFromDirectory, f1, expected, True, True)
expected = []
testGetFilesFromDirectory(teFileHandler.getFilesFromDirectory, f2, expected, True, True)
expected = []
testGetFilesFromDirectory(teFileHandler.getFilesFromDirectory, f3, expected, True, True)
expected = []
testGetFilesFromDirectory(teFileHandler.getFilesFromDirectory, f4, expected, True, True)

#print repr(teFileHandler.getFilesFromDirectory(d3,True))

###################
## Final Results ##
###################

print totalCount, "tests."
print passCount, "passes."
print failCount, "failures."