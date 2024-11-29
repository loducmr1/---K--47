import matplotlib.pyplot as plt 
from sklearn import datasets 
from sklearn.cluster import KMeans 
import sklearn.metrics as sm 
import pandas as pd 
import numpy as np 
iris =datasets.load_iris() 
X=pd.DataFrame(iris.data) 
X.columns=['Sepal_Length','Sepal_Width', 'Petal_length', 'Petal_Width'] 
y=pd.DataFrame(iris.target) 
y.columns=['target'] 
plt.figure(figsize=(14,7)) 
colormap=np.array(['red','lime','black'])
plt.subplot(1,2,1) 
plt.scatter(X.Sepal_Length,X.Sepal_Width,c=colormap[y.target],s=40) 
plt.title('Sepal') 
plt.subplot(1,2,2) 
plt.scatter(X.Petal_length,X.Petal_Width,c=colormap[y.target],s=40) 
plt.title('Petal') 
model=KMeans(n_clusters=3) 
model.fit(X) 
print(model.labels_) 
plt.subplot(1,2,1) 
plt.scatter(X.Petal_length,X.Petal_Width,c=colormap[y.target],s=40) 
plt.title('Real Classification') 
plt.subplot(1,2,2) 
plt.scatter(X.Petal_length,X.Petal_Width,c=colormap[model.labels_],s=40) 
plt.title( 'KMEANS Classfication') 
