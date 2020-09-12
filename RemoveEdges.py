import sys

inputFileName = sys.argv[1]
outputFileName = sys.argv[2]
cutOffEValue = float(sys.argv[3])

f = open(inputFileName, 'rt')
fn = open(outputFileName, 'w')

line = f.readline()
while line:
	if ":" in line and " " in line:
		row = line.split(":")
		if float(row[1]) < cutOffEValue:
			fn.write(line)
	else:
		fn.write(line)
	line = f.readline()

f.close()
fn.close()
