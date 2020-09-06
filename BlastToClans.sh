#!/bin/bash

# Get the directory where this script is
SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"

inFile="$1"
baseInFile=$(basename ${inFile%.*})
outPath=$(dirname "$inFile")
BlastDB="$outPath/$baseInFile.BlastDB"
BlastOut="$outPath/$baseInFile.csv"
CLANSFile="$outPath/$baseInFile.clans"
numThreads=$(nproc)             # Get the number of the currently available processing units to this process, which maybe less than the number of online processors
numSeqs=$(grep -c ">" $inFile)
eValue="10.0"
task="blastp-fast"

#echo $inFile
#echo $baseInFile
#echo $BlastDB
#echo $outPath
#echo $BlastOut
#echo $numThreads

#makeblastdb -in "$inFile" -dbtype prot -out "$BlastDB"
#blastp -task "$task" -evalue "$eValue" -max_target_seqs "$numSeqs" -db "$BlastDB" -query "$inFile" -outfmt "6 qseqid sseqid evalue" -out "$BlastOut" -num_threads "$numThreads"
python "$DIR/blast2clans.py" "$BlastOut" "$CLANSFile"
