## 0xMirror

A python script to create the Mirror of an entire hard disk for the OS X operating system.

The script creates a 0 byte directory structure for the entire hard disk.


## Build instructions

$ sudo python mirror.py

## Note

sudo should be used as superuser rights are required to make a folder at location /Users.

Enter the corresponding path for the root user.

After runnung the script the directory structure of the entire hard disk is contained in the folder named Backup located at /Users.

It is recommended that the Backup folder should not be created anywhere else

## Screenshot

![ScreenShot](/OS X Mirror/shot.png)