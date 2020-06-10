# using this page as a guide https://towardsdatascience.com/identify-top-topics-using-word-cloud-9c54bc84d911
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import rcParams
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
import numpy as np

file = r'C:/Users/jdeed/OneDrive - University of Exeter/Peroxisome-Targeted BPs/Bacterial sequence files/2020-06-05 Bacterial_proteins_positive_SKL (Processed).csv'
outputlocation = r''
ouputname = r''
df = pd.read_csv(file)

# joining all of the words into a single string does not work if there
# are any NA values present, so I performed the dropna operation on the 
# df to remove any rows that contain NA
df = df.dropna()
# join all words into single string, necessary to convert all to same case 
# (lower here)
all_bacterial_descriptions = ' '.join(df['Description'].str.lower())

#add stopwords (i.e. words I don't want to include to the STOPWORDS parameter)

stopwords = ['family', 
             'family protein',
             'hypothetical', 
             'binding',             
             'protein',
             'domain',
             'multispecies',
             'containing',
             'containing protein',
             'family protein',
             'binding protein',
             'domain containing'] + list(STOPWORDS)
# generate wordcloud 
wordcloud = WordCloud(stopwords=stopwords, background_color="white", max_words=1000).generate(all_bacterial_descriptions)
# use rc Params to define the size of the figure
rcParams['figure.figsize'] = 10,20
plt.imshow(wordcloud)
plt.axis("off")
plt.show()