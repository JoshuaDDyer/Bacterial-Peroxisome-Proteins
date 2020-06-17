import pandas as pd
import gzip
from Bio import SeqIO
import glob

# input folder
inputfolder = r'D:\Bacterial Protein Sequences\ncbi-genomes-2020-06-05'
#output folder
outputpath = r'D:\Bacterial Protein Sequences\ncbi-genomes-2020-06-05'
# output filename
totaldfoutputname = '2020-06-05 Total bacterial genes'
nuniqueoutputname = '2020-06-05 Number of unique genes'
# make empty df to append results to
collateddfcolumns = ["Identifyer","Description","Sequence"]
collated_df = pd.DataFrame(columns = collateddfcolumns)

filelist = glob.glob(inputfolder + '/*protein.faa.gz')
for i, file in enumerate(filelist):
    identifyer = []
    sequence = []
    description = []
    print('protcessing file {}, this is file {} of {}'.format(file, i +1, len(filelist)))
    with gzip.open(file, "rt") as handle:
        # now append the sequence and identifyer to the open lists
        for record in SeqIO.parse(handle, "fasta"):
            identifyer.append(record.id)
            # note that I have converted the fasta to a string here (else it
            # adds a comma between each amino acid)
            sequence.append(str(record.seq))
            description.append(record.description)
       #append to a df then change column names and set the index to the identifyer
# note that .T transposes the data 
        df = pd.DataFrame(data = [identifyer,description,sequence]).T
        df.columns = ['Identifyer','Description','Sequence']
        # append to collated df
        collated_df = collated_df.append(df)   
# save this df containing every bacterial gene
collated_df.to_csv("{}/{}.csv".format(outputpath,totaldfoutputname), header = True, index = None)
# Determine the number of unique values and save that to a series and export as
# .csv
unique = collated_df.nunique()
uniqueseries = pd.Series(unique)
uniqueseries.to_csv("{}/numberuniquevalues.csv".format(outputpath))

