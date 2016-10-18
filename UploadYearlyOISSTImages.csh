#!/bin/csh

set ptk = "/Users/belcher/AwsFiles/NewEarl.pem"
cd ./Images/Yearly

#Upload all of the images
scp -i $ptk ./620/* ubuntu@107.20.157.228:/var/www/Images/oissta-annual-nnvl/620/
scp -i $ptk ./1000/* ubuntu@107.20.157.228:/var/www/Images/oissta-annual-nnvl/1000/
scp -i $ptk ./diy/* ubuntu@107.20.157.228:/var/www/Images/oissta-annual-nnvl/diy/
scp -i $ptk ./hd/* ubuntu@107.20.157.228:/var/www/Images/oissta-annual-nnvl/hd/
scp -i $ptk ./hdsd/* ubuntu@107.20.157.228:/var/www/Images/oissta-annual-nnvl/hdsd/

#Now for local cleanup
rm ./*/oissta*

exit