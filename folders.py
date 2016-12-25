import os


p1 = os.path.dirname(os.path.abspath(__file__))
print p1

p1 = p1 + "/../../"
dirs = os.listdir(p1)
for x in dirs:
	print x


"""

path = "/home"
dirs = os.listdir("/home")

file_ = dirs[0]
print file_
path = path + "/" + file_

dirs = os.listdir(path)
#for file in dirs:
#   print file
"""
