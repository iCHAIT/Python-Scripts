import os
import subprocess
import shutil


user = os.getenv("SUDO_USER")


# Enter the corresponding Username, Eg... /Users/chaitanyagupta/
src_root = "/Users/"+user+"/"
dest_root = "/Users/Backup/"


if os.path.exists(dest_root):
    shutil.rmtree(dest_root)


ignore_folders = ['.git', 'lib', 'env', 'bin', 'Library']


for cur_fol, dirs, files in os.walk(src_root):

    for ignore in ignore_folders:
        if ignore in dirs:
            dirs.remove(ignore)

    dest_dir = cur_fol.replace(src_root, dest_root)

    for dirname in dirs:
        destination = os.path.join(dest_dir, dirname)

        if not os.path.exists(destination):
            os.makedirs(destination)

    for filename in files:
        temp = os.path.join(cur_fol, filename)
        destination = os.path.join(dest_dir, filename)
        open(destination, "w").close()
        stinfo = os.stat(temp)
        os.utime(destination, (stinfo.st_atime, stinfo.st_mtime))
