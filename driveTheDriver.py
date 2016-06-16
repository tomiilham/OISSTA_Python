#!/usr/bin/python

###This module builds a c-shell script to reprocess monthly and/or yearly images

import numpy as np
import os, subprocess


ofilename = 'monthly_catchup.csh'
ofile = open(ofilename,'w')
ofile.write('#!/bin/csh')
ofile.write("\n")

sname = 'oissta_monthly_driver.py'

#years = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
years = ['2016']

#months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
months = ['01', '02', '03', '04']

#imgsize = ['620', '1000', 'DIY', 'HD', 'HDSD']
imgsize = ['HD', 'HDSD']

for i in range(len(years)):
	yyyy = years[i]
	for j in range(len(months)):
		for k in range(len(imgsize)):
			cmd = "/usr/bin/python "+sname+' '+yyyy+months[j]+" "+imgsize[k]
			ofile.write(cmd)
			ofile.write("\n")

ofile.close()

cmd = 'chmod 755 '+ofilename
subprocess.call(cmd, shell=True)




###Yearly driver
ofilename = 'yearly_catchup.csh'
ofile = open(ofilename,'w')
ofile.write('#!/bin/csh')
ofile.write("\n")

sname = 'oissta_yearly_driver.py'
years = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
imgsize = ['620', '1000', 'DIY', 'HD', 'HDSD']

for i in range(len(years)):
	yyyy = years[i]
	for k in range(len(imgsize)):
		cmd = "/usr/bin/python "+sname+' '+yyyy+" "+imgsize[k]
		ofile.write(cmd)
		ofile.write("\n")

ofile.close()

cmd = 'chmod 755 '+ofilename
subprocess.call(cmd, shell=True)

