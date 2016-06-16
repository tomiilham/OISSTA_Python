#!/usr/bin/python

import matplotlib as mpl
mpl.use('Agg')
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os, datetime, sys,subprocess
import numpy as np
#import _imaging

def int2str(mm):
	if(mm == '00'): ms = 'No Data'
	if(mm == '01'): ms = 'January'
	if(mm == '02'): ms = 'February'
	if(mm == '03'): ms = 'March'
	if(mm == '04'): ms = 'April'
	if(mm == '05'): ms = 'May'
	if(mm == '06'): ms = 'June'
	if(mm == '07'): ms = 'July'
	if(mm == '08'): ms = 'August'
	if(mm == '09'): ms = 'September'
	if(mm == '10'): ms = 'October'
	if(mm == '11'): ms = 'November'
	if(mm == '12'): ms = 'December'
	return ms


fdate = sys.argv[1]   #(expects format like: 201301)
yyyy = fdate[0:4]
mm = fdate[4:]
ms = int2str(mm)
labeldate = ms+' '+yyyy
if(mm == '00'): labeldate = ms 
figdpi = 72

imgsize = sys.argv[2]  #(expects 620, 1000, DIY, HD, or HDSD )

cmd = "/usr/bin/python ./oissta_monthly_map.py "+fdate+" "+imgsize
subprocess.call(cmd, shell=True)


if(imgsize == '620' or imgsize == '1000' or imgsize == 'DIY'):
	cmd = "/usr/bin/python ./oissta_monthly_colorbar.py "+fdate+" "+imgsize
	subprocess.call(cmd,shell=True)

if not os.path.isdir('../Images/Monthly'):
	cmd = 'mkdir ../Images/Monthly'
	subprocess.call(cmd,shell=True)
if not os.path.isdir('../Images/Monthly/'+imgsize):
	cmd = 'mkdir ../Images/Monthly/'+imgsize.lower()
	subprocess.call(cmd,shell=True)


if(imgsize == '620' or imgsize == '1000'):
	im1 = Image.open("temporary_map.png")
	im2 = Image.open("temporary_cbar.png")
	im3 = Image.new('RGBA', size = (im1.size[0], im1.size[1]+im2.size[1]))
	im3.paste(im2, (0,im1.size[1]))
	im3.paste(im1, (0,0))
	imgw = str(im3.size[0])
	imgh = str(im3.size[1])
	img_path = '../Images/Monthly/'+imgsize+'/'
	img_name = 'oissta-monthly-nnvl--'+imgw+'x'+imgh+'--'+yyyy+'-'+mm+'-00.png'
	pngfile = img_path+img_name
	print "Saving "+pngfile
	im3.save(pngfile)


if(imgsize == 'DIY'):
	im1 = "./temporary_map.png"
	imgs = Image.open(im1)
	imgw = str(imgs.size[0])
	imgh = str(imgs.size[1])
	img_path = '../Images/Monthly/'+imgsize.lower()+'/'
	img_name = 'oissta-monthly-nnvl--'+imgw+'x'+imgh+'--'+yyyy+'-'+mm+'-00.png'
	cmd = 'mv '+im1+' '+img_name
	subprocess.call(cmd,shell=True)
	im2 = "./temporary_cbar.eps"
	cbar_name = 'oissta-monthly-nnvl--'+yyyy+'-'+mm+'-00_colorbar.eps'
	cmd = 'mv '+im2+' '+cbar_name
	subprocess.call(cmd,shell=True)	
	cmd1 = 'zip oissta-monthly-nnvl--'+imgw+'x'+imgh+'--'+yyyy+'-'+mm+'-00.zip '+img_name+' '+cbar_name+' noaa_logo.eps '
	subprocess.call(cmd1,shell=True)
	cmd2 = 'mv oissta-monthly-nnvl--'+imgw+'x'+imgh+'--'+yyyy+'-'+mm+'-00.zip '+img_path
	subprocess.call(cmd2,shell=True)
	cmd3 = 'rm '+img_name+' '+cbar_name
	subprocess.call(cmd3,shell=True)
	
if(imgsize == 'HD'):
	im1 = Image.open("temporary_map.png")
	imgw = str(im1.size[0])
	imgh = str(im1.size[1])
	draw = ImageDraw.Draw(im1)
	fntpath = '/usr/local/share/fonts/truetype/msttcorefonts/Trebuchet_MS.ttf'
	if(mm != '00'): 
		fnt1 = ImageFont.truetype(fntpath, 25)
		draw.text((224,810), ms+' '+yyyy, (0,0,0), font=fnt1)
		fnt2 = ImageFont.truetype(fntpath, 14)
		ttext = "Compared to 1981-2010 average"
		draw.text((223,838), ttext, (0,0,0), font=fnt2)
	if(mm == '00'): 
		fnt1 = ImageFont.truetype(fntpath, 25)
		draw.text((224,810), ms, (0,0,0), font=fnt1)
	#Add the colorbar
	cbar_orig = Image.open('SSTA.colorbar_HD.png')
	bbox = (1,1,726,49)
	cbar_orig = cbar_orig.crop(bbox)
	old_size = cbar_orig.size
	new_size = (old_size[0]+2,old_size[1]+2)
	cbar_im = Image.new("RGB", new_size)
	cbar_im.paste(cbar_orig, ((new_size[0]-old_size[0])/2,
                      (new_size[1]-old_size[1])/2))
	im1.paste(cbar_im, (596,865))
	
	fnt3 = ImageFont.truetype(fntpath, 48)
	text1 = "Cooler"
	text2 = "Warmer"
	draw.text((645,915), text1, (0,0,0), font=fnt3)
	draw.text((1100,915), text2, (0,0,0), font=fnt3)
	
	draw.polygon([(630,955), (615,945), (630,935)], fill="black", outline="black")
	draw.polygon([(1285,955), (1300,945), (1285,935)], fill="black", outline="black")
	
	img_path = '../Images/Monthly/'+imgsize.lower()+'/'
	img_name = 'oissta-monthly-nnvl--'+imgw+'x'+imgh+'hd--'+yyyy+'-'+mm+'-00.png'
	pngfile = img_path+img_name
	print "Saving "+pngfile
	im1.save(pngfile)
	
	
if(imgsize == 'HDSD'):
	im1 = Image.open("temporary_map.png")
	imgw = str(im1.size[0])
	imgh = str(im1.size[1])
	draw = ImageDraw.Draw(im1)
	fntpath = '/usr/local/share/fonts/truetype/msttcorefonts/Trebuchet_MS.ttf'
	if(mm != '00'): 
		fnt1 = ImageFont.truetype(fntpath, 25)
		draw.text((390,642), ms+' '+yyyy, (0,0,0), font=fnt1)
		fnt2 = ImageFont.truetype(fntpath, 14)
		ttext = "Compared to 1981-2010 average"
		draw.text((390,670), ttext, (0,0,0), font=fnt2)
	if(mm == '00'): 
		fnt1 = ImageFont.truetype(fntpath, 25)
		draw.text((390,642), ms, (0,0,0), font=fnt1)
	
	#Add the colorbar
	cbar_orig = Image.open('SSTA.colorbar_HD.png')
	bbox = (1,1,726,49)
	cbar_orig = cbar_orig.crop(bbox)
	old_size = cbar_orig.size
	new_size = (old_size[0]+2,old_size[1]+2)
	cbar_im = Image.new("RGB", new_size)
	cbar_im.paste(cbar_orig, ((new_size[0]-old_size[0])/2,
                      (new_size[1]-old_size[1])/2))
	im1.paste(cbar_im, (596,740))
	
	fnt3 = ImageFont.truetype(fntpath, 48)
	text1 = "Cooler"
	text2 = "Warmer"
	draw.text((645,791), text1, (0,0,0), font=fnt3)
	draw.text((1100,791), text2, (0,0,0), font=fnt3)
	
	draw.polygon([(630,830), (615,820), (630,810)], fill="black", outline="black")
	draw.polygon([(1285,830), (1300,820), (1285,810)], fill="black", outline="black")
	
	img_path = '../Images/Monthly/'+imgsize.lower()+'/'
	img_name = 'oissta-monthly-nnvl--'+imgw+'x'+imgh+'hdsd--'+yyyy+'-'+mm+'-00.png'
	pngfile = img_path+img_name
	print "Saving "+pngfile
	im1.save(pngfile)

