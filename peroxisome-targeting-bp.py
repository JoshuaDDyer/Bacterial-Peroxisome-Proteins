import gzip
from Bio import SeqIO
import pandas as pd
import glob

filelist = glob.glob(r'C:\Users\jdeed\OneDrive - University of Exeter\Peroxisome-Targeted BPs\Bacterial sequence files\mycobacteria protein fasta files\test' 
          + "/*protein.faa.gz")

collateddfcolumns = ["Identifyer","Sequence"]
collated_df = pd.DataFrame(columns = collateddfcolumns)
collated_df.set_index("Identifyer", inplace = True)
print(collated_df)

for file in filelist:     
    # open a list for the identifyer and for the sequence
    identifyer = []
    sequence = []
    # open faa.gz file
    with gzip.open(file, "rt") as handle:
        # now append the sequence and identifyer to the open lists
        for record in SeqIO.parse(handle, "fasta"):
            identifyer.append(record.id)
            # note that I have converted the fasta to a string here (else it
            # adds a comma between each amino acid)
            sequence.append(str(record.seq))
    #append to a df then change column names and set the index to the identifyer
    df = pd.DataFrame(data = [identifyer,sequence]).T
    df.columns = ['Identifyer','Sequence']
    df.set_index("Identifyer", inplace = True)
    SKLmask = df["Sequence"].str.upper().str.endswith("SKL")
    skldf = df[SKLmask]
    print (skldf)
    collated_df.append(skldf)           
print(collated_df)
