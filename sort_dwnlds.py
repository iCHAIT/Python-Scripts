import os
import shutil

user = os.getenv("USER")
dir = "/Users/"+user+"/Desktop/test/"
# dir = "/Users/"+user+"/Downloads/"

try:
    os.chdir(dir)
    for files in os.listdir("."):
        print files
        extn = files.split(".")[0]
        print extn
        dirname = extn.upper()
        if os.path.isdir(dir+dirname):
            shutil.move(dir+files, dir+dirname)

        else:
            os.mkdir(dir+dirname)
            shutil.move(dir+files, dir+dirname)

except IOError:
    print "Error in reading file"
