import sys
import csv

header = """
<param>
maxmove=0.1
pval=1
usescval=false
complexatt=true
cooling=1.0
currcool=1.0
attfactor=10.0
attvalpow=1
repfactor=10.0
repvalpow=1
dampening=1.0
minattract=1.0
cluster2d=false
blastpath=''
formatdbpath=''
showinfo=false
zoom=1.0
dotsize=10
ovalsize=10
groupsize=4
usefoldchange=false
avgfoldchange=false
colorcutoffs=0.0;0.1;0.2;0.3;0.4;0.5;0.6;0.7;0.8;0.9;
colorarr=(230;230;230):(207;207;207):(184;184;184):(161;161;161):(138;138;138):(115;115;115):(92;92;92):(69;69;69):(46;46;46):(23;23;23):
</param>
<rotmtx>
1.0;0.0;0.0;
0.0;1.0;0.0;
0.0;0.0;1.0;
</rotmtx>
<seq>
"""

inputFileName = sys.argv[1]
outputFileName = sys.argv[2]

f = open(inputFileName, 'rt')
reader = csv.reader(f, delimiter='\t')
listNamePos = []
listName = []
count = 0
print("Create list of sequence names with indeces.")
for row in reader:
	if row[0] not in listName:
		listName.append(row[0])
		listNamePos.append([row[0],count])
		count += 1

f.close()

fn = open(outputFileName, 'w')
fn.write('sequences={}\n'.format(count))
fn.write(header)

for r in listNamePos:
	fn.write(">{}\nX\n".format(r[0]))

fn.write("</seq>\n<hsp>\n")

print("List with names and indeces has been created")
print("Creating links")

f = open(inputFileName, 'rt')
reader = csv.reader(f, delimiter='\t')
for row in reader:
#	print(row)
	pos1 = 0
	pos2 = 0
	for r in listNamePos:
		if r[0] == row[0]:
			pos1 = r[1]
		if r[0] == row[1]:
			pos2 = r[1]
	fn.write("{0} {1}:{2}\n".format(pos1,pos2,row[2]))
fn.write("</hsp>\n")

f.close()
print("Links have been created")
fn.close()
