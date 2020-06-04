import tarfile

def extractfromtar (file,outputfolder):
# open faa.gz file
    seqfile = tarfile.open(file)
#extract individual fasta.tar files to a folder
    seqfile.extractall(outputfolder)

extractfromtar(r'C:/Users/jdeed/OneDrive - University of Exeter/Peroxisome-Targeted BPs/Bacterial sequence files/Mycobacteria genome_assemblies_prot_fasta.tar',
    r'C:\Users\jdeed\OneDrive - University of Exeter\Peroxisome-Targeted BPs\Bacterial sequence files\mycobacteria protein fasta files')
