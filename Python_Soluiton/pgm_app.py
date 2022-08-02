import sys
import os

Path = sys.argv[1]
os.chdir(Path)

fileNum = 0

# iterate through all file
for file in os.listdir():
    # Check whether file is in text format or not
	if file.endswith(".pgm"):
		file_path = f"{Path}\{file}"
		fileNum += 1
print(fileNum)
