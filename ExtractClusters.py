
import os
import sys

inputFileName = sys.argv[1]
outputFolderName = sys.argv[2]

if not os.path.isdir(outputFolderName):
	os.makedirs(outputFolderName)

f = open(inputFileName, 'rt')

counter = -1
sequences = {}

line = f.readline()
while line and not line == "<seq>\n":
	line = f.readline()

line = f.readline()

while line and not line == "</seq>\n":
	if line[0]==">":
		counter += 1
		sequences[counter] = line
	elif len(line) > 0:
		sequences[counter] += line

	line = f.readline()

f.close()

f = open(inputFileName, 'rt')

line = f.readline()
while line and not line == "<seqgroups>\n":
	line = f.readline()

line = f.readline()

while line and not line == "</seqgroups>\n":
	splitLine = line.split("=")
	if splitLine[0] == "name":
		outFile = os.path.join(outputFolderName, splitLine[1].replace(" ", "").strip() + ".fasta")
	if splitLine[0] == "numbers":
		clusterFile = open(outFile, 'w')
		seqIDNumbers = splitLine[1].strip().strip(";").split(";")
		for seqID in seqIDNumbers:
			index = int(seqID)
			clusterFile.write(sequences[index]);
		clusterFile.close()

	line = f.readline()

f.close()
