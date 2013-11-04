#te_fileHandler
import os

def isFile(filepath):
	#check if the filepath is just a single filepath
	#if yes, return true, not false
	return os.path.isfile(filepath)

def isDirectory(filepath):
	#check if filepath is isDirectory
	#if yes return true, else false
	return os.path.isdir(filepath)

def getFilesFromDirectory(filepath,recursive=False):
	pass