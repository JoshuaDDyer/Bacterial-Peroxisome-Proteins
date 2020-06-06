import tarfile

file = r'D:/Bacterial Protein Sequences/2020-06-06 genome_assemblies_prot_fasta.tar'
outputfolder = r'D:\Bacterial Protein Sequences'



def extractfromtar (file,outputfolder):
# open faa.gz file
    seqfile = tarfile.open(file)
#extract individual fasta.tar files to a folder
    seqfile.extractall(outputfolder)

extractfromtar(file,outputfolder)
print("extraction complete")