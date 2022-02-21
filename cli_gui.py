import tkinter as tk 
from tkinter import filedialog
import time, functions  

OPTIONS = 1,2,9

def printMenu():
	""" Prints user menu """
	print("*** Micro Backup ***")
	print("1 - Copy destination folder and subfolders to target folder")
	print("2 - Copy all media from source folder to target folder")
	print("9 - Quit")


def prompt():
	""" Ask user for proper input """
	while True:
		option = input("Choose an option: ")
		if int(option.isnumeric()) and int(option) in OPTIONS:
			return int(option)
			break
		else: 
			print("Incorrect option")

def selection(option):
	if option == 1:
		fullFolder()
	elif option == 2:
		allMedia()
	elif option == 9:
		print("Quiting...")
	else:
		print("Unexpected error")


def yesNo(askString):
	""" Ask user yes or no """
	while True:
		print(askString)
		answer = input("Y/N?: ")
		if answer.lower()[0] == "y":
			return True 
			break
		elif answer.lower()[0] == "n":
			return False 
			break
		else:
			print("Wrong answer") 

def fullFolder():
	""" menu option 1 """
	src, dst = askFolders()
	compress = yesNo("Compress?")
	functions.fromFolder_toFolder(src, dst, compress)
	print("*** BACKUP COMPLETED ***")

def allMedia():
	""" menu option 2 """
	src, dst = askFolders()
	functions.media_backup(src, dst)
	print("*** MEDIA BACKUP COMPLETED ***")


def askFolders():
	""" Asks the user for a folder, pops up the folder selection """
	root = tk.Tk()
	root.withdraw()
	print("Prompting for source folder...")
	time.sleep(2.5)
	src = filedialog.askdirectory()
	print("Prompting for destination folder...")
	time.sleep(2.5)
	dst = filedialog.askdirectory()	 
	return src, dst


