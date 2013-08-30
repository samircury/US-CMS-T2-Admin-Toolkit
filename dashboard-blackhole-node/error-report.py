#!/usr/bin/python

import json
import urllib2
import pdb
import time
# http://dashb-cms-job.cern.ch/dashboard/request.py/jobstatus2?user=&site=T2_US_Caltech&submissiontool=&application=&activity=&status=aborted&check=terminated&tier=&sortby=user&ce=&rb=&grid=&jobtype=&submissionui=&dataset=&submissiontype=&task=&subtoolver=&genactivity=production&outputse=&appexitcode=&accesstype=&date1=2013-7-18+11%3A17%3A59&date2=2013-7-19+11%3A17%3A59&count=1634&offset=0&exitcode=&fail=&cat=&len=5000&prettyprint


# Get all failures

hoursOffset = 18 

def failDistLast(hours):

	#FIXME: The delta T algorithm doesnt work if the difference between the current hour and the offset is smaller than 0. (midnight)
	finalTime = time.strftime("%Y-%m-%d+%H")+"%3A"+time.strftime("%M")
	initTime = time.strftime("%Y-%m-%d+")+str(int(time.strftime("%H"))-hoursOffset)+"%3A"+time.strftime("%M")
	
	#print "%s %s" % (initTime, finalTime)
	
	dashbUrl = "http://dashb-cms-job.cern.ch/dashboard/request.py/jobstatus2?user=&site=T2_US_Caltech&submissiontool=&application=&activity=analysis&status=app-failed&check=terminated&tier=&sortby=activity&ce=&rb=&grid=&jobtype=&submissionui=&dataset=&submissiontype=&task=&subtoolver=&genactivity=&outputse=&appexitcode=&accesstype=&date1=%s&date2=%s&count=9999&offset=0&exitcode=all&fail=all&cat=&len=5000&prettyprint" % (initTime, finalTime)
	
	response = urllib2.urlopen(dashbUrl)
	
	# check 200 or bail
	
	dashbjson = json.loads(response.read())
	
	
	failureDistribution = {}
	#print dashbjson['jobs']
	for job in dashbjson['jobs']:
		if failureDistribution.has_key(job['WNHostName']):
			failureDistribution[job['WNHostName']] += 1
		else :
			failureDistribution[job['WNHostName']] = 1
	
	return failureDistribution

#print dashbjson

def findAvgFail(failDist):
	total = 0
	for node in failDist.keys():
		total += failDist[node]
	avg = total/len(failDist.keys())
	return avg

def findTotalFail(failDist):
	total = 0
	for node in failDist.keys():
	       total += failDist[node]
	return total


def findBadNodes(failDist) :
	badNodes = []
	totalFail = findTotalFail(failDist)
	print "Total failures: %d" % totalFail
	print "================================="
	th = 0.1 ###### FAILURE THRESHOLD FOR BAD NODES
        for node in failDist.keys():
		failShare = float(failDist[node])/float(totalFail)
		if failShare > th:
			print "node %s is bad with %f failures" % (node, failShare)
			

failDist = failDistLast(hoursOffset)

for node in failDist.keys():
	print "%s had %d failures" % (node, failDist[node])

print "================================="
print "average failure rate is %d" % findAvgFail(failDist)


findBadNodes(failDist)



# Extract site, make sure of site

# Make array (or hash) of nodes

# Iterate, count

# Present distribution

# Depending on option make histogram, check CMSSW environment before.


