import os
import shutil

user = os.getenv("USER")
dir = "/Users/"+user+"/Downloads/"


def sort(f_type):
    try:
        dirname = f_type.upper()
        os.chdir(dir)
        for files in os.listdir("."):

            if files.endswith(f_type):

                if os.path.isdir(dir+dirname):
                    shutil.move(dir+files, dir+dirname)

                else:
                    os.mkdir(dir+dirname)
                    shutil.move(dir+files, dir+dirname)

        return

    except IOError:
        print "Error in reading file"

sort("scpt")
sort("dmg")
sort("mp3")
sort("rpm")
sort("zip")
sort("pdf")
sort("doc")
sort("gz")
sort("jpg")
sort("flv")
sort("tar")
sort("torrent")
sort("txt")
sort("zip")
sort("exe")
sort("bz")
sort("dotx")
sort("csv")
sort("iso")
sort("download")
sort("pkg")
sort("html")
sort("ics")
sort("whl")
sort("rar")
sort("epub")
sort("png")
sort("odp")
sort("ppt")
