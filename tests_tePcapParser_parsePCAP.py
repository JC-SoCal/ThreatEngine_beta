import tePcapFileParser

passCount = 0
failCount = 0
totalCount = 0

def testParsePCAP(function, varible, expected, negate):
	global passCount
	global failCount
	global totalCount

	totalCount += 1
	if negate:
		status,data = function(varible)
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
		status,data = function(varible)
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
f1 = "testdata\\pcaps\\small.pcap"

###########################
## Create the test cases ##
###########################

print "Positive PCAP File Test"
expected = {'domains': ['yahoo.com'], 'ips': ['192.168.106.255', '98.138.253.109', '66.96.162.150', '192.168.106.2', '192.168.106.130', '98.139.183.24', '206.190.36.45', '8.8.8.8'], 'filename': ['testdata\\pcaps\\small.pcap']}
testParsePCAP(tePcapFileParser.parsePCAP, f1, expected, False)

###################
## Final Results ##
###################

print totalCount, "tests."
print passCount, "passes."
print failCount, "failures."