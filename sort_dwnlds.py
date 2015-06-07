import os
import shutil

user = os.getenv("USER")
# dir = "/Users/"+user+"/Desktop/hat/"
dir = "/Users/"+user+"/Downloads/"

try:
    os.chdir(dir)
    for files in os.listdir(dir):
        if not files.startswith('.'):    # Ignoring hidden files
            if os.path.isfile(files):
                extn = os.path.splitext(files)[1].replace('.', '')
                dirname = extn.upper()
                if os.path.isdir(dir+dirname):
                    if os.path.isfile(dir+dirname+"/"+files):
                        print "Could not move "+dir+files+" it already exist in "+dir+dirname+"/"
                        continue
                    else:
                        shutil.move(dir+files, dir+dirname)

                else:
                    os.mkdir(dir+dirname)
                    shutil.move(dir+files, dir+dirname)
    print "All Done!"

except IOError:
    print "Error in reading file"