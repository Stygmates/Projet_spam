'''
Created on 15 avr. 2016

@author: tarek
'''
from File_management import Load, Save
from File_management.Save import save_csv
from File_management.Load import load_csv
from KMeans.Kmeans import Kmeans

if __name__ == '__main__':
    print("Hello main method")
    
    save_csv(load_csv())