import gzip
from Bio import SeqIO
import pandas as pd

# open a list for the identifyer and for the sequence
identifyer = []
sequence = []
# open faa.gz file
with gzip.open(r'C:/Users/jdeed/OneDrive - University of Exeter/Peroxisome-Targeted BPs/Bacterial sequence files/mycobacteria protein fasta files/ncbi-genomes-2020-06-03/GCF_010731775.1_ASM1073177v1_protein.faa.gz',
           "rt") as handle:
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
df.head(5)
SKLmask = df["Sequence"].str.upper().str.endswith("SKL")
print(df[SKLmask])
