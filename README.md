## OS X Mirror

A python script to create the Backup of an entire hard disk for the OS X operating system.

The script creates a 0 byte directory structure for the hard disk.


## Build Instructions

Enter the corresponding path for the root user.

$sudo python mirror.py 

After doing the above,directory structure of the entire hard disk will be contained in a folder named Backup created at location /Users.


## Note

sudo need to be written before the script is run because you need SuperUser rights to create a folder at location /Users.

It is recommended that you do not create this backup folder anywhere else.


## Screenshot

Your /Users will look something like this.

![ScreenShot](photo.png)