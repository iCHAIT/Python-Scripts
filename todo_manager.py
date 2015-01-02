import random 

with open('TODO.txt', "r+") as f:
	lines = f.readlines()
	print lines
	a = str(random.choice(lines))	
	print a
	f.seek(0)
	f.truncate()
	for line in lines:
  		if line != a:
   			f.write(line)

   					

    