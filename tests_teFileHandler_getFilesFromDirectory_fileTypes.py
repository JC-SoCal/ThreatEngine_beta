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
d1 = "testdata\\teFileHandler_fileTypes"
d2 = "testdata\\teFileHandler_fileTypes\\dir1"

###########################
## Create the test cases ##
###########################
print "Get files from directory, non-recursive"
expected = ['testdata\\teFileHandler_fileTypes\\file1.txt', 'testdata\\teFileHandler_fileTypes\\file2.log', 'testdata\\teFileHandler_fileTypes\\file3.csv', 'testdata\\teFileHandler_fileTypes\\file4.pcap']
testGetFilesFromDirectory(teFileHandler.getFilesFromDirectory, d1, expected, False, False)
expected = ['testdata\\teFileHandler_fileTypes\\dir1\\file5.txt', 'testdata\\teFileHandler_fileTypes\\dir1\\file6.log', 'testdata\\teFileHandler_fileTypes\\dir1\\file7.csv', 'testdata\\teFileHandler_fileTypes\\dir1\\file8.pcap']
testGetFilesFromDirectory(teFileHandler.getFilesFromDirectory, d2, expected, False, False)

print "Get files from directory, recursive"
expected = ['testdata\\teFileHandler_fileTypes\\file1.txt', 'testdata\\teFileHandler_fileTypes\\file2.log', 'testdata\\teFileHandler_fileTypes\\file3.csv', 'testdata\\teFileHandler_fileTypes\\file4.pcap', 'testdata\\teFileHandler_fileTypes\\dir1\\file5.txt', 'testdata\\teFileHandler_fileTypes\\dir1\\file6.log', 'testdata\\teFileHandler_fileTypes\\dir1\\file7.csv', 'testdata\\teFileHandler_fileTypes\\dir1\\file8.pcap']
testGetFilesFromDirectory(teFileHandler.getFilesFromDirectory, d1, expected, True, False)
expected = ['testdata\\teFileHandler_fileTypes\\dir1\\file5.txt', 'testdata\\teFileHandler_fileTypes\\dir1\\file6.log', 'testdata\\teFileHandler_fileTypes\\dir1\\file7.csv', 'testdata\\teFileHandler_fileTypes\\dir1\\file8.pcap']
testGetFilesFromDirectory(teFileHandler.getFilesFromDirectory, d2, expected, True, False)

###################
## Final Results ##
###################

print totalCount, "tests."
print passCount, "passes."
print failCount, "failures."