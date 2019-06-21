# batch_file_rename.py
# Created by Alan Gui on 6/20/2019

"""
This will batch rename a group of files in a given directory,
once you pass the current and new extensions
批量重命名指定目录下面所有文件的后缀名
"""

import os
import argparse

def batch_rename(work_dir, old_ext, new_ext):
	# Get all file name under the given directory
	for filename in os.listdir(work_dir):
		# Get the file extension
		split_file = os.path.splitext(filename)
		file_ext = split_file[1]
		# Check file's extension
		if file_ext == old_ext:
			newfile = split_file[0] + new_ext

			# Rename the file
			os.rename(
				os.path.join(work_dir, filename), 
				os.path.join(work_dir, newfile)
			)


def get_parser():
	# Analyse the input argument
	parser = argparse.ArgumentParser(description=
				'change extension of files in the given directory')
	parser.add_argument('work_dir', metavar='WORK_DIR', type=str, nargs=1, 
						help='the directory where to change extensions')
	parser.add_argument('old_ext', metavar='OLD_EXT', type=str, nargs=1, 
						help='old extension')
	parser.add_argument('new_ext', metavar='NEW_EXT', type=str, nargs=1, 
						help='new extension')
	return parser

def main():
	# Add command line argument
	parser = get_parser()
	args = vars(parser.parse_args())

	# Set the variable word_dir with the first argument passed
	work_dir = args['work_dir'][0]
	# Set the variable old_ext with the second argument passed
	old_ext = args['old_ext'][0]
	if old_ext[0] != '.':
		old_ext = '.'+  old_ext
	# Set the variable new_ext with the third argument passed
	new_ext = args['new_ext'][0]
	if new_ext[0] != '.'
		new_ext = '.' + new_ext

	batch_rename(work_dir, old_ext, new_ext)


if __name__ == '__main__':
	main()