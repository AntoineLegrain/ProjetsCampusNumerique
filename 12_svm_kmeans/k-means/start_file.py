# -*- coding: utf-8 -*-



#### make data
from sklearn.datasets import make_blobs
X, y = make_blobs(n_samples=100, centers=5, n_features=2,random_state=1)


class KMeans_perso():
    import numpy as np
    import matplotlib.pyplot as plt
    
    def __init__(self, number_clusters=3, n_init=1):
        """Init function"""
        self.number_clusters = number_clusters
        self.n_init = n_init



    def _random_c(self, X):
        """ Return number_clusters random centroids from dataset X in order 
        to inialize K-means classification. Retruns nothing, array C is directly modified."""
        self.C[0]=X[np.random.randint(low=0, high=len(X), size=self.number_clusters)]
    
    def _euclidian(A,B):
        """ Return the euclidian distance between A and B."""
        # return (A-B)**2
        return np.linalg.norm(A-B)
    
    def _min_euclidian(self,X):
        """ Given centroids in C[0], dataset X,
        labels the data according to their cluster."""
        labels = np.argmin(((X - self.C[0][:, np.newaxis])**2).sum(axis=2), axis=0)
        return labels
    
    #### Calculate the euclidean distance between each point and each of the centroids, and assign label.
    
    
    def _mean_points_in_clusters(self,X):
        """Define new centroids in C[0] being the barycenter of all data points
        in each cluster."""
        for cluster in range(0,self.number_clusters):
            if X[:,0][self.labels==cluster].size != 0:
                self.C[0][cluster] = X[self.labels==cluster].mean(axis=0)
    
    
    def _inertia_calculation(self,X):
        """ Returns inertia of classification. 
        Inertia is the mean squared distance between each instance and 
        its closest centroid.""" 
        inertia=0
        for cluster in range(0,self.number_clusters):
            # inertia+=euclidian(X[labels==cluster],C[0][cluster])
            inertia+=((X[self.labels==cluster]-self.C[0][cluster])**2).sum(axis=1).sum()
        return inertia/len(X)
            
    def plot_clusters(self,X):
        """ Plot clusters a,d their centroids. Clusters will be sorted by labels."""
        colors=('g','b','pink','y','m','slategray','cyan','silver','violet','gold')
        for i in range(0,self.C.shape[1]):
            plt.scatter(X[:,0][self.labels==i],X[:,1][self.labels==i],c=colors[i],alpha=0.3)
        for i in range(0,len(self.C[0])):
            plt.scatter(self.C[0][i][0],self.C[0][i][1],c='r',marker='2')
        plt.xlabel('X1')
        plt.ylabel('X2')
    #### expected function
    
    def _k_means_algo(self,X):
        """Probably not optimal K-means algorithm. The best inertia will be selected out of
        n_init iterations."""
        #inertia is set anormally high to be tested for lower value.
        inertia=float(10**6)
        #Creating a numpy array for labels.
        self.labels=np.zeros(len(X))
        #Creating a numpy array for sotring centroids. Two lines for after/before comparison
        self.C=np.zeros((2,self.number_clusters,2)) 
        for i in range(0,self.n_init):
            SameCentroids=False
            #Storing random centroids in first line of array C
            self._random_c(X) 
            #Creating clusters, filling with points closest to centroids. Shape is number of clusters * length X. If filled with 0, no points.
            self.labels=self._min_euclidian(X)
            
            while SameCentroids==False:
                #Second line of C becomes the centroids to compare to see if the algorithm had converged
                self.C[1]=self.C[0]
                #Defining new centroids as average of points in each clusters :
                self._mean_points_in_clusters(X)
                self.labels=self._min_euclidian(X)
                #Stopping criteria: if centroids before and after are identical, we have converged.
                if (self.C[0]==self.C[1]).all():
                    SameCentroids=True
            #If inerita for this loop is lower than the ones before, we store optimal results.
            if self._inertia_calculation(X)<inertia:
                inertia=self._inertia_calculation(X)
                Copt=self.C
                labels_opt=self.labels
        return Copt,labels_opt

    
    def fit(self, X):
        '''fit function: trains a kmean solver'''
        assert isinstance(X, np.ndarray), 'X must be a numpy array'
        self.C,self.labels=self._k_means_algo(X)
        return self.labels

    def predict(self, X):
        '''Use previously trained kmean to predict the classes for X'''
        try:
            self.C
        except AttributeError:
            raise Exception('can not predict using an unfitted kmean')
        
        return self._min_euclidian(X)
            

#### main
# C,labels=k_means_algo(X,number_clusters,15)
# plot_clusters(C,X,labels)