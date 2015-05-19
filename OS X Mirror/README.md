## 0xMirror

A python script to create the Mirror of an entire hard disk for the OS X operating system.

The script creates a 0 byte directory structure for the entire hard disk.


## Run the script

$ sudo python mirror.py

sudo should be used,as superuser rights are required to make a folder at location /Users.

After running the script the directory structure of the entire hard disk is contained in the folder named Backup that is created at location /Users.

It is recommended that the Backup folder should not be created anywhere else.

## Screenshot

Your /Users should look like this...

![ScreenShot](/OS X Mirror/shot.png)

A folder named Backup will be created.

## TODO

Implement the script using scandir() instead of walk.

## Credits

Thanks for the idea [Shadab Zafar](https://github.com/dufferzafar)