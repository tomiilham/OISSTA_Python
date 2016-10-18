#!/bin/csh

set ptk = "/Users/belcher/AwsFiles/NewEarl.pem"
cd ./Images/Monthly

#Upload all of the images
scp -i $ptk ./620/* ubuntu@107.20.157.228:/var/www/Images/oissta-monthly-nnvl/620/
scp -i $ptk ./1000/* ubuntu@107.20.157.228:/var/www/Images/oissta-monthly-nnvl/1000/
scp -i $ptk ./diy/* ubuntu@107.20.157.228:/var/www/Images/oissta-monthly-nnvl/diy/
scp -i $ptk ./hd/* ubuntu@107.20.157.228:/var/www/Images/oissta-monthly-nnvl/hd/
scp -i $ptk ./hdsd/* ubuntu@107.20.157.228:/var/www/Images/oissta-monthly-nnvl/hdsd/

#Now for local cleanup
rm ./*/oissta*
