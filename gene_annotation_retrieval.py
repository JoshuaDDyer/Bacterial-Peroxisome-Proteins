from Bio import SeqIO
import pandas as pd

inputfile = r'C:/Users/jdeed/OneDrive - University of Exeter/Peroxisome-Targeted BPs/Bacterial sequence files/test/test_positive_SKL.csv'

df = pd.read_csv(inputfile)
print(df)

print(df.dtypes)