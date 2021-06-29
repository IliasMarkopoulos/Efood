# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""





import pandas as pd
import numpy as np
import sklearn as sk
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler




# Reading the dataset that will be used for clustering
# it is an  aggregate per customer for Breakfast orders
# the query used for the creation of the dataset is 
#https://github.com/IliasMarkopoulos/Efood/blob/main/Clustering_dataset.sql





#Reading the csv in pyhon. In a production environment we could directly use the sql code

df_import = pd.read_csv(r"C:\Users\Ilias\Desktop\bq-results-20210628-215130-vimdrod198gt.csv")




#creating some graphs and a summary table in order to better understand data 



df_import.describe()


plt.hist(df_import['total_amount'], color = 'blue', edgecolor = 'black',
         bins = int(180/5))
plt.show()



plt.scatter(df_import['total_amount'], df_import['Breakfast_orders'],  alpha=0.5)
plt.xlabel('total_amount')
plt.ylabel('Breakfast_orders')
plt.show()





# as we saw in the summary there was cases with 0 order amount, we will remove these cases as it is most likely an error in data

df_import = df_import.loc[df_import['avg_amount']>0]


#keep specific variables that will be used for clustering
#made some tests with avg_amount instead of total, but clusters are more clearly defined with total amount

df = df_import[['user_id','total_amount','Breakfast_orders']]


#scaling data in order for K means to work properly


X = df.values
X = np.nan_to_num(X)

sc = StandardScaler()

cluster_data = sc.fit_transform(X)




#finding the optimal number of clusters
Sum_of_squared_distances = []
K = range(1,15)
for k in K:
    km = KMeans(n_clusters=k)
    km = km.fit(cluster_data)
    Sum_of_squared_distances.append(km.inertia_)
    
plt.plot(K, Sum_of_squared_distances, 'bx-')
plt.xlabel('k')
plt.ylabel('Sum_of_squared_distances')
plt.title('Elbow Method For Optimal k')
plt.show()

#as can be seen from the plot the optimal number of clusters is 4


#running kmeans clustering for 4 clusters


clusters = 4
model = KMeans(init = 'k-means++', 
               n_clusters = clusters, 
               n_init = 12)
model.fit(cluster_data)

labels = model.labels_


# adding the clusters in the original dataset
df_import['cluster_num'] = labels



#getting the summaries of each segment
#df.groupby('cluster_num').agg({'total_amount':['sum','mean'],'Breakfast_orders':'mean'})
df_import.groupby('cluster_num').agg({'total_amount':['sum','mean'],'avg_amount':'mean','Breakfast_orders':'mean'})


#export and excel file of the results

df_import.to_excel(r"C:\Users\Ilias\Desktop\clusters2.xlsx")