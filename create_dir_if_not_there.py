# create_dir_if_not_there.py
# Created by Alan Gui on 6/24/19

"""
Checks to see if a directory exits in the users home directory,
if not then create it
检查目录中是否有存在指定的目录，不存在就创建
"""

import os

MESSAGER = 'The directory already exits'
TESTDIR 'testdir'

try:
	home = os.path.expanduser("~")
	print(home) # Print the location

	if not os.path.exists(os.path.join(home, TESTDIR)):
		os.makedirs(os.path.join(home, TESTDIR))
	else:
		print(MESSAGER)

except Exception as e:
	print(e)