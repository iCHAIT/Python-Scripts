import os,subprocess

f = open('mirror.txt', 'w+')
for root, dirs, files in os.walk("/Users"):
	for name in files:
		a = os.path.join(root, name)
		trial = list(a)
		trial[1] = "+"
		a = "/Users/admin/Desktop/mirror" + "".join(trial)
        if not os.path.exists(a):
            subprocess.call(['touch', os.path.join(dirs, a)])
		#issue here(only one file is being made).
        f.write(a + "\n")
	for name in dirs:
		a = os.path.join(root, name)
		trial = list(a)
		trial[1] = "+"
		a = "/Users/admin/Desktop/mirror" + "".join(trial)
		f.write(a + "\n")
		if not os.path.exists(a):
			os.makedirs(a)
f.close()
