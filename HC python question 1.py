
#Required libraries
import numpy as np
import pandas as pd 

import matplotlib.pyplot as plt
import seaborn as sns

#Loading the dataset

dataset = pd.read_excel("C:/Users/rohika/OneDrive/Desktop/360digiTMG assignment/Datasets_Kmeans/EastWestAirlines (1).xlsx" , sheet_name ='data')
dataset.head()

#EDA calculation

dataset= dataset.rename(columns={'ID#':'ID', 'Award?':'Award'})


dataset1 =  dataset.drop(['ID','Award'], axis=1)
dataset1.head(2)
#Normalization function

def norm_func(i):
    x = (i-i.min())	/ (i.max()-i.min())
    return (x)

#normalised data
df_norm = norm_func(dataset1.iloc[:,0:])
df_norm.describe()

# for creating dendrogram 
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch 

z = linkage(df_norm, method = "complete", metric = "euclidean")

#Ploting the dendogram

# Dendrogram
plt.figure(figsize=(15, 8));plt.title('Hierarchical Clustering Dendrogram');plt.xlabel('Index');plt.ylabel('Distance')
sch.dendrogram(z, 
    leaf_rotation = 0,  # rotates the x axis labels
    leaf_font_size = 10 # font size for the x axis labels
)
plt.show()


# Now applying AgglomerativeClustering choosing 5 as clusters from the above dendrogram
from sklearn.cluster import AgglomerativeClustering

h_complete = AgglomerativeClustering(n_clusters = 3, linkage = 'complete', affinity = "euclidean").fit(df_norm) 
h_complete.labels_

cluster_labels = pd.Series(h_complete.labels_)

dataset['clust'] = cluster_labels # creating a new column and assigning it to new column 

dataset2 = dataset.iloc[:, [12,0,1,2,3,4,5,6,8,9,10,11]]
dataset2.head()

# Aggregate mean of each cluster
dataset2.iloc[:, 1:].groupby(dataset1.clust).mean()

# creating a csv file 
dataset2.to_csv("EastWest.csv", encoding = "utf-8")

import os
os.getcwd()

