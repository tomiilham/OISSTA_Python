#!/usr/bin/python

'''*************************************************************************************************
Program: oisstamaindriver.py

Usage: ./oisstamaindriver.py [args]

Synopsis:
This script will check for updated NNVL OISST monthly data. If new data exist, the 
most recent monthly maps will be created. The user has the option to pass arguments in the form of
year and month to force the script to generate maps for a specific month (year). Otherwise, the
script will attempt to process the "previous" month's maps.

*************************************************************************************************'''

import datetime, subprocess, sys, urllib
from dateutil.relativedelta import *



if __name__ == '__main__':

	
	
#If no "date" args are passed in, find and process the previous month from the current date	
	if(len(sys.argv) == 1):
		date_last_month = datetime.datetime.now() - relativedelta(months=1)
		yyyy = date_last_month.year
		mm = date_last_month.month
		stryyyy = str(yyyy)
		if(mm < 10): strmm = '0'+str(mm)
		if(mm > 9): strmm = str(mm)
		
		newimg = "SSTA.monthly."+stryyyy+strmm+".color.png"
	
		url = "ftp://ftp.nnvl.noaa.gov/View/SSTA/Images/Color/Monthly/"+newimg
		output = urllib.urlretrieve(url, newimg)
		cmd = "mv "+newimg+" ../Images/Monthly/Orig/"
		subprocess.call(cmd,shell=True)			
		
		isz = ['620', '1000', 'DIY', 'HD', 'HDSD']
		for i in xrange(len(isz)):
			cmd = 'python oissta_monthly_driver.py '+stryyyy+strmm+' '+isz[i]
			subprocess.call(cmd, shell=True)
		cmd = "./UploadDsImages.csh"
		subprocess.call(cmd, shell=True)

	if(len(sys.argv) == 2):
		idate = sys.argv[1]
		if(len(idate) == 4):
			newimg = "SSTA.yearly."+idate+".color.png"
			url = "ftp://ftp.nnvl.noaa.gov/View/SSTA/Images/Color/Yearly/"+newimg
			output = urllib.urlretrieve(url, newimg)
			cmd = "mv "+newimg+" ../Images/Yearly/Orig/"
			subprocess.call(cmd,shell=True)			
		
			isz = ['620', '1000', 'DIY', 'HD', 'HDSD']
			for i in xrange(len(isz)):
				cmd = 'python oissta_yearly_driver.py '+idate+' '+isz[i]
				subprocess.call(cmd, shell=True)
			cmd = "./UploadMonthlyOISSTImages.csh"
			subprocess.call(cmd, shell=True)
		if(len(idate) == 6):
			newimg = "SSTA.monthly."+idate+".color.png"
			url = "ftp://ftp.nnvl.noaa.gov/View/SSTA/Images/Color/Monthly/"+newimg
			output = urllib.urlretrieve(url, newimg)
			cmd = "mv "+newimg+" ../Images/Monthly/Orig/"
			subprocess.call(cmd,shell=True)			
		
			isz = ['620', '1000', 'DIY', 'HD', 'HDSD']
			for i in xrange(len(isz)):
				cmd = 'python oissta_monthly_driver.py '+idate+' '+isz[i]
				subprocess.call(cmd, shell=True)
			cmd = "./UploadYearlyOISSTImages.csh"
			subprocess.call(cmd, shell=True)
	
		