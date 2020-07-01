import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
outputfolder = r'C:\Users\jdeed\OneDrive - University of Exeter\Peroxisome-Targeted BPs\Bacterial sequence files'

# _step 1_ - calculate the number of times the terms DNA, oxidoreductase
# and transcription occur in the database of SKL positive bacterial proteins. 
sklpositivecsv = r'C:/Users/jdeed/OneDrive - University of Exeter/Peroxisome-Targeted BPs/Bacterial sequence files/2020-06-05 Bacterial_proteins_positive_SKL (Processed).csv'
skldf = pd.read_csv(sklpositivecsv)
#  identify cells in 'Description' column that contain oxidoreductase,dna and 
# transcriptional
SKLoxredpositive = skldf['Description'].str.lower().str.contains('oxidoreductase')
SKLdnapositive = skldf['Description'].str.lower().str.contains('dna')
SKLtranspositive = skldf['Description'].str.lower().str.contains('transcriptional')
# now count each of these and assign to variable
SKLoxredcount = SKLoxredpositive.sum()
SKLdnacount = SKLdnapositive.sum()
SKLtranscount = SKLtranspositive.sum()
# count total
SKLtotal = skldf['Description'].count()
# now create percentages
SKLoxredpercent = SKLoxredcount / SKLtotal * 100 
SKLdnapercent = SKLdnacount / SKLtotal * 100 
SKLtranspercent  = SKLtranscount / SKLtotal * 100 
# add all variables to list
SKLlist = [SKLtotal,
           SKLoxredcount,
           SKLdnacount,
           SKLtranscount,
           SKLoxredpercent,
           SKLdnapercent,
           SKLtranspercent]
# create df using SKLlist
SKLcolumnnames = ['Total SKL',
                  'SKL+Oxred Positive',
                  'SKL+DNA Positive',
                  'SKL+Transcriptional Positive',
                  'SKL+Oxred Percent of TotalSKL',
                  'SKL+DNA Percent of TotalSKL',
                  'SKL+Transcriptional Percent of TotalSKL']
screenedSKLdf = pd.DataFrame(data = SKLlist).T
screenedSKLdf.columns = SKLcolumnnames
# export 
screenedSKLdf.to_csv('{}/SKLpositiveDescriptionProbe.csv'.format(outputfolder), index = None)

# step 2: load in the file containing the number of total bacterial proteins
# per gz.protein.faa file and identify totals and means
totalpositivecsv = r'C:/Users/jdeed/OneDrive - University of Exeter/Peroxisome-Targeted BPs/Bacterial sequence files/2020-06-05 descriptions containing oxidoreductase.csv'
totalpositivedf = pd.read_csv(totalpositivecsv)
describetotalpositivedf = totalpositivedf.describe()
describetotalpositivedf.to_csv('{}/totaldescriptionprobe.csv'.format(outputfolder))

