#!/usr/bin/python

import json
import urllib2
import pdb
import time
# http://dashb-cms-job.cern.ch/dashboard/request.py/jobstatus2?user=&site=T2_US_Caltech&submissiontool=&application=&activity=&status=aborted&check=terminated&tier=&sortby=user&ce=&rb=&grid=&jobtype=&submissionui=&dataset=&submissiontype=&task=&subtoolver=&genactivity=production&outputse=&appexitcode=&accesstype=&date1=2013-7-18+11%3A17%3A59&date2=2013-7-19+11%3A17%3A59&count=1634&offset=0&exitcode=&fail=&cat=&len=5000&prettyprint


# Get all failures

hoursOffset = 1

finalTime = time.strftime("%Y-%m-%d+%H")+"%3A"+time.strftime("%MA00")
initTime = time.strftime("%Y-%m-%d+")+str(int(time.strftime("%H"))-hoursOffset)+"%3A"+time.strftime("%MA00")

dashbUrl = "http://dashb-cms-job.cern.ch/dashboard/request.py/jobstatus2?user=&site=T2_US_Caltech&submissiontool=&application=&activity=&status=aborted&check=terminated&tier=&sortby=user&ce=&rb=&grid=&jobtype=&submissionui=&dataset=&submissiontype=&task=&subtoolver=&genactivity=production&outputse=&appexitcode=&accesstype=&date1=%s&date2=%s&count=1634&offset=0&exitcode=&fail=&cat=&len=5000&prettyprint" % (initTime, finalTime)

print dashbUrl

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

print failureDistribution


#print dashbjson



# Extract site, make sure of site

# Make array (or hash) of nodes

# Iterate, count

# Present distribution

# Depending on option make histogram, check CMSSW environment before.


