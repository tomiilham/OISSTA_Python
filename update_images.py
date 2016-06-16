#!/usr/bin/python

from datetime import *
import os, urllib, sys, time, subprocess


yyyy = sys.argv[1]
monstr = ["01","02","03","04","05","06","07","08","09","10","11","12"]
monint = [1,2,3,4,5,6,7,8,9,10,11,12]
this_yyyy = str(time.localtime().tm_year)
this_month = time.localtime().tm_mon
this_week = int(datetime.today().strftime("%U"))

		
		
		
#downlaod all monthly images from input year and put them in the Monthly/Orig folder
for i in range(12):
	if(yyyy == this_yyyy and monint[i] < this_month):
		fname = "SSTA.monthly."+yyyy+monstr[i]+".color.png"
		url = "ftp://ftp.nnvl.noaa.gov/View/SSTA/Images/Color/Monthly/"+fname
		urllib.urlretrieve(url, "tmp.png")
		cmd = "mv tmp.png ../Images/Monthly/Orig/"+fname
		subprocess.call(cmd,shell=True)
	if(yyyy != this_yyyy):
		fname = "SSTA.monthly."+yyyy+monstr[i]+".color.png"
		url = "ftp://ftp.nnvl.noaa.gov/View/SSTA/Images/Color/Monthly/"+fname
		urllib.urlretrieve(url, "tmp.png")
		cmd = "mv tmp.png ../Images/Monthly/Orig/"+fname
		subprocess.call(cmd,shell=True)
		

#download the yearly file (in not current year) and put it in the Yearly/Orig folder
if (yyyy != this_yyyy):
	fname = "SSTA.yearly."+yyyy+".color.png"
	url = "ftp://ftp.nnvl.noaa.gov/View/SSTA/Images/Color/Yearly/"+fname
	urllib.urlretrieve(url, "tmp.png")
	cmd = "mv tmp.png ../Images/Yearly/Orig/"+fname
	subprocess.call(cmd,shell=True)
