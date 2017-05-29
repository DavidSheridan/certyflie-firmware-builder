#!/usr/bin/env python

import os
import io

# extensions of files that need their eol converted
file_extensions = ['.gpr', '.ads', '.adb']

# traverses through the specified base directory and its child directories
# converting the line endings to unix for files that match the
# required format.
#
# @param base_dir {string} - path for the base directory
#
def convert_line_endings(base_dir):
	# initialise a stack of directory names
	directories = [base_dir]

	# search for files while there are still directories to search
	while len(directories) != 0:
		directory = directories.pop()
		
		# check for files and child directories in the current directory
		os.chdir(directory)
		filenames = os.listdir(directory)
		for filename in filenames:
			# check if the current file is actually a file or a directory
			if os.path.isdir(filename):
				# push directories to the directory stack
				directories.append(os.path.join(os.getcwd(),filename))
			else:
				# replace line endings for the file if necessary
				for extension in file_extensions:
					if filename.endswith(extension):
						replace_line_endings(filename)
	print('done')

# converts the line endings in the specified file to be unix line endings
#
# @param filename {string} - the name of the file
#	
def replace_line_endings(filename):
	print('convert line endings for: ', filename)
	
	# read the lines from the specified file
	with open(filename, 'rU', encoding='ansi') as file:
		lines = file.readlines()
	file.close()

	# write lines back into the file with the new line endings
	with io.open(filename, 'w', newline='\n', encoding='ansi') as file:
		for line in lines:
			file.write(line)
		file.close()