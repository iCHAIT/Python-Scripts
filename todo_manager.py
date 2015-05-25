import random

with open('TODO.txt', "r+") as f:  # I've kept my TODO list in TODO.txt
    lines = f.readlines()
    task = str(random.choice(lines))
    print task

    f.seek(0)
    f.truncate()

    for line in lines:
        if line != task:
            f.write(line)
