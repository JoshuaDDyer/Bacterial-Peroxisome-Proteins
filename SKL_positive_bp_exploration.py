# the aim of this code is to parse through the fasta.gz files 
# and identify the number of proteins with descriptions that contain keywords

import gzip
from Bio import SeqIO
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
import glob

# input folder
inputfolder = r'D:\Bacterial Protein Sequences\ncbi-genomes-2020-06-05'
#output folder
outputpath = r'D:\Bacterial Protein Sequences\ncbi-genomes-2020-06-05'
# output filename
outputname = '2020-06-05 descriptions containing oxidoreductase'

filelist = glob.glob(inputfolder + "/*protein.faa.gz")

# list of terms to search for
searchfor = ["oxidoreductase","protein"]

# create new df to append results to
collated_df = pd.DataFrame()

print(collated_df)

for i, file in enumerate(filelist):
    print("this is file {} of {}".format(i+1,len(filelist)))
    #open lists to append data from fasta file to
    identifyer = []
    sequence = []
    description = []
    totalnumberofsequenceslist = []
    oxidasereducase_containinglist = []
    dna_containinglist = []
    # use gzip to open protein.faa.gz file and append to lists then make into df
    with gzip.open(file, "rt") as handle:
            for record in SeqIO.parse(handle, "fasta"):
                identifyer.append(record.id)
                # note that I have converted the fasta to a string here (else it
                # adds a comma between each amino acid)
                sequence.append(str(record.seq))
                description.append(record.description)
            df = pd.DataFrame(data = [identifyer,description,sequence]).T
            df.columns = ['Identifyer','Description','Sequence']
            # count total number of values in the description series of the df
            total = df['Description'].count()
            # count number of proteins that contain the term "oxidoreductase" in 
            # the description - note that we have changed all strings to lowercase
            # to prevent case-based misidentification            
            oxredpositive = df['Description'].str.lower().str.contains("oxidoreductase")
            numberoxredpositive = oxredpositive.sum()
            # for comparison, count number of proteins that contain term 'DNA'
            dnapositive = df['Description'].str.lower().str.contains("dna")
            numberdnapositive = dnapositive.sum()
            # for comparison count number of proteins that contain term 'transcriptional'
            transpositive = df['Description'].str.lower().str.contains("transcriptional")
            numbertranspositive = transpositive.sum()
            # calculate percentages of each
            oxredpercent = numberoxredpositive / total * 100
            dnapercent = numberdnapositive / total * 100
            transpercent = numbertranspositive / total * 100
            # list of results
            results = [file,
                       total,
                       numberoxredpositive,
                       numberdnapositive,
                       numbertranspositive,
                       oxredpercent,
                       dnapercent,
                       transpercent]
            # had loads of trouble appending this to empty df, ended up converting to series 
            # then appending that
            resultsseries = pd.Series(results)
    collated_df = collated_df.append(resultsseries, ignore_index = True)
# change column names
collated_df.columns = ["filename",
                       "total sequences",
                       "oxidoreductase_containing",
                       "dna_containing",
                       "transcriptional_containing",
                       "percentage oxred",
                       "percentage dna",
                       "percentage transcriptional"]
# export 
collated_df.to_csv("{}/{}.csv".format(outputpath,outputname))


