'''
Created on 20 avr. 2016

@author: tarek
'''
from Point.Point3d import Point3d
from math import sqrt
from File_management.Save import *
from File_management.Load import *


def barycentre3d(tab,taille):
    p = Point3d(0.0,0.0,0,2)
    for i in range(0,taille):
        p.x = p.x + tab[i].x
        p.y = p.y + tab[i].y
        p.z = p.z + tab[i].z
    p.x = p.x/taille
    p.y = p.y/taille
    p.z = p.z/taille
    
    return p
'''
    p1 est-il plus proche de p2 ou de p3 ?
'''
def plus_proche3d(p1,p2,p3):
    
    distance1 = distance3d(p1, p2)
    distance2 = distance3d(p1, p3)
    
    if (distance1 <= distance2):
        return p2
    else:
        return p3
    
def distance3d(p1,p2):
    return sqrt((p1.x-p2.x)*(p1.x-p2.x)+(p1.y-p2.y)*(p1.y-p2.y)+(p1.z-p2.z)*(p1.z-p2.z))
    

'''
Dis quel point est plus proche de p3
1 pour p1
2 pour p2
'''
def plus_proche_nombre3d(p1,p2,p3):
    distancep1 = distance3d(p1, p3)
    distancep2 = distance3d(p2, p3)
    if (distancep1 <= distancep2):
        return 1
    else:
        return 2
    
def indice_barycentre_plus_proche_tab3d(tab,p1):
    if(tab!=[]):
        if(len(tab) == 1):
            return 0
        j = 0
        p = tab[0]
        for i in range(0,len(tab)):
            if(plus_proche_nombre3d(p,tab[i],p1) == 2):
                j = i
                p = tab[i]
        return j
    
'''
    creer un tableau qui contient les tableaux contenant les points les plus proches des barycentres tabcluster  
'''
def rangement3d(tab,tabcluster):
    temp = []
    for i in tabcluster:
        temp.append([])
        
    for j in tab:
        temp[indice_barycentre_plus_proche_tab3d(tabcluster, j)].append(j)
    return temp

def affichertabcluster3d(tab):
    print("[")
    for line in tab:
        print("[",end=' ')
        for i in line:
            print("(" + str(i.x) + "," + str(i.y) + "," + str(i.z) + ")",end=' ')
        print("]")
    print("]")

def affichertab3d(tab):
    for line in tab:
        print("(" + str(line.x) + "," + str(line.y) + "," + str(line.z) + ")")
'''
    renvoie un tableau avec les barycentres de tous les cluster du tableau
'''    
def tabbarycentre3d(tab):
    temp = []
    for line in tab:
        if line == []:
            return []
        bary = barycentre3d(line, len(line))
        temp.append(bary)
    return temp

def notequal(tab,tab1):
    if len(tab) != len(tab1):
        return -1
    for i in range(0,len(tab)):
        if tab[i].x != tab1[i].x or tab[i].y !=tab1[i].y or tab[i].z !=tab1[i].z:
            return 1
    return 0

'''
    k = nb cluster a creer
    tab = tableau simple des points
'''
def KMeans3d(tab,k):
    tempbar = []
    tempbar.append(tab[0])
    for i in range(1,k):
        tempbar.append(tab[i])
    tabcluster = rangement3d(tab, tempbar)
    tempbarold = tempbar[:]
    tempbar = tabbarycentre3d(tabcluster)
   
    while notequal(tempbar,tempbarold) == 1:
         
        tabcluster = rangement3d(tab, tempbar)
        tempbarold = tempbar[:]
        tempbar = tabbarycentre3d(tabcluster)
    return tabcluster


def runcolumnmin(tab,column):
    valmin=tab[1][column]
    for line in range(2,len(tab)-1):
        if line != []:
            valmin= min(tab[line][column],valmin)
    return valmin

def diff(tab, column):
    valmax=tab[1][column]
    valmin=tab[1][column]
    for line in range(2,len(tab)-1):
        if line != []:
            valmax= max(tab[line][column],valmax)
            valmin= min(tab[line][column],valmin)
    return float(valmax)-float(valmin)
'''
    normalise un tableau simple de float
'''

def normalisationcolonne(tab):
    mini = min(tab)
    maxi = max(tab)
    temp = []
    
    for line in tab:
        temp.append((float(line - mini))/(maxi-mini))
    return temp
'''
    normalisation d'un tableau de tableau
'''
def normalisation3d(tab):
    temp=[]
    col0=[]
    col1=[]
    col2=[]
    colspam=[]
    for line in tab:
        col0.append(float(line[0]))
        col1.append(float(line[1]))
        col2.append(float(line[2]))
        colspam.append(int(line[3]))
    col0n = normalisationcolonne(col0)
    col1n = normalisationcolonne(col1) 
    col2n = normalisationcolonne(col2) 
    for i in range(0,len(col0n)):
        tempt = []
        tempt.append(col0n[i])
        tempt.append(col1n[i])
        tempt.append(col2n[i])
        tempt.append(colspam[i])
        temp.append(tempt)
    return temp    
'''
    parametre : tableau de Kmeans entierement trie, n en pourcentage
    retourne un tableau avec n% des extremite en moins
'''
            
def cluster_range(tab):
    bary = barycentre3d(tab,len(tab))
    temp = []
    i = 0
    for line in tab:
        temp2 = []
        d = distance3d(bary, line)
        temp2.append(d)
        temp2.append(i)
        i= i+1
        temp.append(temp2)
    temp.sort(cmp=None, key=None, reverse=False)
    
    temp3 = []
    for elem in temp:
        temp3.append(tab[elem[1]])
    return temp3

def tab_cluster_range(tab):
    temp = []
    for line in tab:
        temp.append(cluster_range(line))
    return temp

def extraction(tab,N):
    for line in tab:
        i = 0
        for j in line:
            i = i+1
        indice = i*N/100
        print(indice)
        temp = []
        for k in range(0,indice):
            temp.append(line[k])
    return temp

def moyennecol(tab, numcol):
    i = 0.
    m = 0.
    for line in tab:
        i+=1
        m = m + line[numcol]

    return m/i

        

if __name__ == '__main__':
    print("Hello main method")
    
    dataset = load_csv()
    save_csv(dataset)
    cols = [18,2,4,57]
    tabfiltre = filtrage(dataset, cols)
    tabnormalise = normalisation3d(tabfiltre)
    afficher(tabnormalise)
    tabpoints = (transformer3(tabnormalise))
    affichertab3d(tabpoints)
    tabcluster = KMeans3d(tabpoints, 2)
    #affichertabcluster3d(tabcluster)
    
    