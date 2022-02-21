import os, sys, shutil, mimetypes, cli_gui


# Get file extensions for media backpup
def get_extensions(type):
	for ext in mimetypes.types_map:
		if mimetypes.types_map[ext].split('/')[0] == type:
			yield ext

FILE_EXTENSIONS = list(get_extensions('video')) \
+ list(get_extensions('audio')) \
+ list(get_extensions('image'))

# Quick look at current working dir
def pwd():
	print(os.getcwd())

def fromFolder_toFolder(src, dst, compress):
	"""Backup all data an folders from folder to target folder
	   First argument src folder, second is destination folder
	   last is compression, if True will compress to tar"""
	if compress:
		print("Working on it please be patient...")
		compressed_folder = shutil.make_archive(os.path.basename(src), 'gztar', src)
		
		shutil.move(compressed_folder, dst, copy_function=shutil.copy2)
	else:
		print("Working on it please be patient...")
		shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=shutil.copy2, ignore_dangling_symlinks=False, dirs_exist_ok=True)
		

def media_backup(src, dst):
	"""Backup all media (audio, video, images) from folder to target folder"""
	for root, subdirs, files in os.walk(src):
		for item in os.listdir(root):
			file_path = os.path.join(root, item)
			for extension in FILE_EXTENSIONS:
				if file_path.endswith(extension):					
					shutil.copy2(file_path, dst)
					print("Copying... " + os.path.basename(file_path))
				else:
					continue





