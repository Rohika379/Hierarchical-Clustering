

import pandas as pd
import numpy as np

data = pd.read_csv("C:/Users/rohika/OneDrive/Desktop/360digiTMG assignment/h clustering data sets/AutoInsurance.csv")

data.head()

data.shape

#Customer and state is not required 

data.drop(['Customer','State','Effective To Date'],axis=1,inplace=True)
data.head()

#EDA performing
#Checking for null values of the data set
data.isnull().sum()


data.dtypes

cols=data.columns
cols

#Changing the column types

cat_cols=data.select_dtypes(exclude=['int','float']).columns
cat_cols

#Checking the data types
data.dtypes

enc_data=list(cat_cols)
enc_data=enc_data[:]
enc_data

#Importing  library for encoding
from sklearn.preprocessing import LabelEncoder

le=LabelEncoder()

#Defining the function for column transformentation

data[enc_data]=data[enc_data].apply(lambda col:le.fit_transform(col))
data[enc_data].head()

data.head()

# Normalization function
def norm_func(i):
    x = (i-i.mean())/(i.std())
    return (x)

# Normalized data frame 
df_norm = norm_func(data.iloc[:, 1:])
df_norm.describe()

# for creating dendrogram 
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch 
import matplotlib.pylab as plt
z = linkage(df_norm, method = "complete", metric = "euclidean")

# Dendrogram
plt.figure(figsize=(15, 8));plt.title('Hierarchical Clustering Dendrogram');plt.xlabel('Index');plt.ylabel('Distance')
sch.dendrogram(z, 
    leaf_rotation = 0,  # rotates the x axis labels
    leaf_font_size = 10 # font size for the x axis labels
)
plt.show()

from	sklearn.cluster	import	AgglomerativeClustering 
h_complete	=	AgglomerativeClustering(n_clusters=4,	linkage='complete',affinity = "euclidean").fit(df_norm) 

cluster_labels=pd.Series(h_complete.labels_)

data['clust']=cluster_labels # creating a  new column and assigning it to new column 

data.head()

# creating a csv file 
data.to_csv("Auto.csv", encoding = "utf-8")

import os
os.getcwd()




























