import os, subprocess, shutil, sys

if len(sys.argv) != 3:
    print("Usage: mirror [source_directory_root] [destination_directory_root]")
    sys.exit(1)

src_root = str(sys.argv[1])
dest_root =str(sys.argv[2])

if os.path.exists(dest_root):
	shutil.rmtree(dest_root)

ignore_folders = ['.git', 'lib', 'env', 'bin', '.Trash']
ignore_files = ['.DS_Store', '.localized']

for cur_fol, dirs, files in os.walk(src_root):

	for ignore in ignore_folders:
		if ignore in dirs:
			dirs.remove(ignore)

	for ignore in ignore_files:
		if ignore in files:
			files.remove(ignore)

	dest_dir = cur_fol.replace(src_root, dest_root)

	for dirname in dirs:
		destination = os.path.join(dest_dir, dirname)
		if not os.path.exists(destination):
			os.makedirs(destination)

	for filename in files:
		destination = os.path.join(dest_dir, filename)

		open(destination, "w").close()
