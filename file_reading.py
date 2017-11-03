import os

for cwd, sub_folder, files in os.walk("documents"):
	for file in files:
		print("File name:", file)
		f = open(str(cwd + "/" + file), "r")
		print(f.read())
