import pandas as pd
import gzip
from Bio import SeqIO
import glob

# input folder
inputfolder = r'D:\Bacterial Protein Sequences\ncbi-genomes-2020-06-05'
#output folder
outputpath = r'D:\Bacterial Protein Sequences\ncbi-genomes-2020-06-05'
# output filename
outputname = '2020-06-05 Total number of genes'

# make empty df to append results to
collateddfcolumns = ["Identifyer","Description","Sequence"]
collated_df = pd.DataFrame(columns = collateddfcolumns)
filelist = glob.glob(inputfolder + '/*protein.faa.gz')
# set gene counter to 0
genecounter = 0
#open list 
for i, file in enumerate(filelist):
    genelist = []
    print('protcessing file {}, this is file {} of {}'.format(file, i +1, len(filelist)))
    with gzip.open(file, "rt") as handle:
        # now append the identifyer to the open lists
        for record in SeqIO.parse(handle, "fasta"):
            genelist.append(record.id)
    # count number of genes per file
    genesperfile = len(genelist)
    # add this number to counter
    genecounter = genecounter + genesperfile

# convert number of genes to a series for easy export
genenumberseries = pd.Series(genecounter)
# save this series containing every bacterial gene
genenumberseries.to_csv("{}/{}.csv".format(outputpath,outputname), header = True, index = None)
