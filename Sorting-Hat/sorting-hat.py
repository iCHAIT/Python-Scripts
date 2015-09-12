import os
import shutil

user = os.getenv("USER")
# direc = "/Users/"+user+"/Downloads/"
direc = "/Users/"+user+"/Desktop/hat/"


def findExtension(files):
    # Find the extension of the file
    extn = os.path.splitext(files)[1].replace('.', '')
    dirname = extn.upper()
    return dirname


def FileExist(direc, dirname, files):
    # Check if the file to be sorted already exist in the target subdirectory.
    # if it doesn't then move it.
    if os.path.isfile(os.path.join(direc, dirname, files)):
        print "Could not move "+os.path.join(direc, files)+" it already exist in "+os.path.join(direc, dirname)
        return
    shutil.move(os.path.join(direc, files), os.path.join(direc, dirname))


def makeTheDir(files):
    # Make the target sub directory.
    os.mkdir(os.path.join(direc, dirname))
    shutil.move(os.path.join(direc, files), os.path.join(direc, dirname))


try:
    os.chdir(direc)
    for files in os.listdir(direc):
        if not files.startswith('.'):    # Ignoring hidden files
            if os.path.isfile(files):
                dirname = findExtension(files)
                if os.path.isdir(os.path.join(direc, dirname)):
                    FileExist(direc, dirname, files)

                else:
                    makeTheDir(files)
    print "All Done!"

except IOError:
    print "Error in reading file"
