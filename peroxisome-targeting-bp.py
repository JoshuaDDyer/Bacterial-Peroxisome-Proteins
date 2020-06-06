import gzip
from Bio import SeqIO
import pandas as pd
import glob

# input folder
inputfolder = r'D:\Bacterial Protein Sequences\ncbi-genomes-2020-06-05'
#output folder
outputpath = r'D:\Bacterial Protein Sequences\ncbi-genomes-2020-06-05'
# output filename
outputname = 'Bacterial_proteins_positive_SKL'
# make empty df to append results to
collateddfcolumns = ["Identifyer","Description","Sequence"]
collated_df = pd.DataFrame(columns = collateddfcolumns)
# retrieve list of files using glob method
filelist = glob.glob(inputfolder + "/*protein.faa.gz")
print(filelist)
for i, file in enumerate(filelist):     
    print ('Processing file {} of {}'.format(i+1, len(filelist)))
    # open a list for the identifyer and for the sequence
    identifyer = []
    sequence = []
    description = []
    # open faa.gz file
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
    SKLmask = df["Sequence"].str.upper().str.endswith("SKL")
    skldf = df[SKLmask]
    print(skldf)
    # note that pandas append does not happen 'inplace' and so needs to have 
    # it specified that you want to replace the original object with the new 
    # object

    collated_df = collated_df.append(skldf) 

print(collated_df)

# export to .csv
collated_df.to_csv('{}/{}.csv'.format(outputpath,outputname), index = None, header = True)          

