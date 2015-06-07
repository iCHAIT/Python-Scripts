import os
import shutil

user = os.getenv("USER")
direc = "/Users/"+user+"/Downloads/"
# direc = "/Users/"+user+"/Desktop/hat/"


def findExtension():
    extn = os.path.splitext(files)[1].replace('.', '')
    dirname = extn.upper()
    return dirname


def ifFileExist():
    if os.path.isfile(direc+dirname+"/"+files):
        print "Could not move "+direc+files+" it already exist in "+direc+dirname+"/"
        return
    shutil.move(direc+files, direc+dirname)


def makethedir():
    os.mkdir(direc+dirname)
    shutil.move(direc+files, direc+dirname)


try:
    os.chdir(direc)
    for files in os.listdir(direc):
        if not files.startswith('.'):    # Ignoring hidden files
            if os.path.isfile(files):
                dirname = findExtension();
                if os.path.isdir(direc+dirname):
                    ifFileExist();

                else:
                    makethedir();
    print "All Done!"

except IOError:
    print "Error in reading file"
