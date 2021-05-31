

import pandas as pd
#<comp = matplotlib,library for visualization is imported, matplotlib not imported,seaborn
import matplotlib.pylab as plt 

#<comp=read_csv,input file is being read,read_csv() not used;read_excel
crime = pd.read_csv("C:\\Users\\rohika\\OneDrive\\Desktop\\360digiTMG assignment\\h clustering data sets\\crime_data.csv")
#<optional = .columns, Display columns, Columns not displayed
crime.columns
#<optional = .isna, Ckecking for NAs, NAs not checked;optional = .sum, total NAs count
crime.isna().sum()
#optional = .isnull, Checking for NULL values, NULL values not checked; Optional = .sum, total NULL count
crime.isnull().sum()


# Normalization function suing z std. all are continuous data , not considering city variable.
#<comp= function, Normalization fucntion is defined, Function is not Normalised
def norm_func(i):
    x = (i-i.mean())/(i.std())
    return (x)
	  
# Normalized data frame (considering the numerical part of data)
df_norm = norm_func(crime.iloc[:,1:])
#<optional = .describe, analysing data informations like count,

df_norm.describe()

#<comp= scipy.cluster.hierarchy, proper library imported for Hierarchial Cluster Analysis, Library not imported for using Hierarchial Clustering
#<comp= linkage, proper function imported for building a clustering model, linkage function not imported
from scipy.cluster.hierarchy import linkage 

import scipy.cluster.hierarchy as sch # for creating dendrogram 

z = linkage(df_norm, method="complete",metric="euclidean")
#<comp = plt.figure,clusters can be visualized, plt.figure is not used for visualizng clusters
#<comp = .dendrogram, Proper function for visualizing dendrogram, .dendrogram is not used for visualizing
plt.figure(figsize=(15, 5));plt.title('Hierarchical Clustering Dendrogram');plt.xlabel('Index');plt.ylabel('Distance')
sch.dendrogram(
    z,
    leaf_rotation=0.,  # rotates the x axis labels
    leaf_font_size=8.,  # font size for the x axis labels
)
plt.show()

from	sklearn.cluster	import	AgglomerativeClustering 
h_complete	=	AgglomerativeClustering(n_clusters=4,	linkage='complete',affinity = "euclidean").fit(df_norm) 

#<comp = Series, converting the labels to pandas series,Labels not converted to pandas series
cluster_labels=pd.Series(h_complete.labels_)

crime['clust']=cluster_labels # creating a  new column and assigning it to new column 
#<optional = .iloc, rearranging variables using index, Variables are not rearranged
crime = crime.iloc[:,[5,0,1,2,3,4]]
#<optioal = .head, displayinghead of dataset, Head values not displayed
crime.head()

# getting aggregate mean of each cluster
#<comp = groupby, Grouping the clusters and aggregating, Clusters were not grouped
crime.iloc[:,2:].groupby(crime.clust).median()
 
