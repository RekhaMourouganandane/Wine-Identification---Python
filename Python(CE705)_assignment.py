# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 10:29:31 2022

@author: Rekha Muruganantham
"""
'''#1) Class: matrix
You will code a class called matrix, which will have an attribute called array_2d. This attribute is
supposed to be a NumPy array containing numbers in two dimensions. The class matrix must have
the following methods:
(in these, the parameters are in addition to self)'''
import numpy as np
import os
class matrix:
    
    def __init__(self,filename):       
        self.load_from_csv(filename)
        self.standardise()



    def load_from_csv(self,filename):
        self.array_2d = np.empty((0, 0))
        self.array_2d =  np.loadtxt(filename, delimiter=',')       
        return self.array_2d
#Defining the standardise Function (Standarsing the data set using the Formula)

    def standardise(self):
        avg = np.mean(self.array_2d,axis=0)
        ma = np.max(self.array_2d,axis=0)
        mi = np.min(self.array_2d,axis=0)
        for x in range(len(self.array_2d)):
            for y in range(len(self.array_2d[x])):
                self.array_2d[x,y]=(self.array_2d[x,y]-avg[y])/(ma[y]-mi[y])
        return self.array_2d
#get_distance(passing three parameters other _matrix ,weights and Beta value and calculated the distance and finding the min among them) 
 
    
    def get_distance(self, other_matrix,w,Beta):
        
        distance = np.ones((self.centroids.shape[0],1))
        for eachrow in range(self.centroids.shape[0]):
         distance[eachrow]= np.sum(((w**Beta)*(self.centroids[eachrow])-other_matrix)**2)  
     
        
        min = np.min(distance)   
        for i in range(len(distance)):
            if distance[i]==min:
                 return i
#get_count_frequency (This functions has got no parameters and this will return a dictionary)         
                
    def get_count_frequency(self):
        unique, counts = np.unique(self.S, return_counts=True)
        return dict(zip(unique, counts))
#get_initial_weights(This functions has got m parameters, The sum will be equal to one)       
    
def get_initial_weights(m):
    w=np.random.random(m)
    w/=np.sum(w)
    return w

#get_centroids(This function has got three parameters ,which is used to update the k value )

def get_centroids(data,S,K):
    
    output=[] 
    for k in range(K):
        cluster_centroid=[]
        for j in range(S.shape[0]):
            if S[j,0] ==k:
                cluster_centroid.append(obj.array_2d[j])
        output.append(np.mean(np.array(cluster_centroid),axis=0))
    return(np.array(output))
    
#get_groups(This function should have three parameters: a matrix containing the data, and the number of groups
#to be created (K), and a number beta (for the distance calculation).It should return a matrix S)    

def get_groups(obj,K,Beta):
    rows=obj.array_2d.shape[0]
    column=obj.array_2d.shape[1]
    weights=get_initial_weights(column)
    obj.centroids= np.empty((0,0)) 
    obj.S= np.zeros((rows,1))
    obj.centroids= obj.array_2d[np.random.randint(obj.array_2d.shape[0],size=K),:]
    while(True):
        S1= obj.S.copy()
        for i in range(len(obj.array_2d)):
                obj.S[i]= obj.get_distance(obj.array_2d[i],weights,Beta)
        if (obj.S!= S1) .all():
            
            obj.centroids= get_centroids(obj,obj.S,K)
            weights = get_initial_weights(column)
        else:
            return obj

    

    
    
def run_test():
    m = matrix('Data.csv')
    for k in range(2,5):
        for beta in range(11,25):
            S = get_groups(m, k, beta/10)
            print(str(k)+'-'+str(beta)+'='+str(S.get_count_frequency()))


    
if __name__ == "__main__":

    run_test()
                
                
        

    