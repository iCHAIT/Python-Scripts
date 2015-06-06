import os
import shutil

user = os.getenv("USER")
dir = "/Users/"+user+"/Desktop/hat/"
# dir = "/Users/"+user+"/Downloads/"

try:
    os.chdir(dir)
    for files in os.listdir(dir):
        if not files.startswith('.'):    # Ignoring hidden files
            print files
            if os.path.isfile(files):
                extn = files.split(".")[1]
                print extn
                dirname = extn.upper()
                if os.path.isdir(dir+dirname):
                    shutil.move(dir+files, dir+dirname)

                else:
                    os.mkdir(dir+dirname)
                    shutil.move(dir+files, dir+dirname)

except IOError:
    print "Error in reading file"
