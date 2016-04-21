'''
Created on 20 avr. 2016

@author: tarek
'''
from Point.Point import Point
from math import sqrt
from File_management.Save import *
from File_management.Load import *


def barycentre(tab,taille):
    p = Point(0.0,0.0)
    for i in range(0,taille):
        p.x = p.x + tab[i].x
        p.y = p.y + tab[i].y
    p.x = p.x/taille
    p.y = p.y/taille
    
    return p
'''
    p1 est-il plus proche de p2 ou de p3 ?
'''
def plus_proche(p1,p2,p3):
    
    distance1 = distance(p1, p2)
    distance2 = distance(p1, p3)
    
    if (distance1 <= distance2):
        return p2
    else:
        return p3
    
def distance(p1,p2):
    return sqrt((p1.x-p2.x)*(p1.x-p2.x) + (p1.y-p2.y)*(p1.y-p2.y))
    

'''
Dis quel point est plus proche de p3
1 pour p1
2 pour p2
'''
def plus_proche_nombre(p1,p2,p3):
    distancep1 = distance(p1, p3)
    distancep2 = distance(p2, p3)
    if (distancep1 <= distancep2):
        return 1
    else:
        return 2
    
def indice_barycentre_plus_proche_tab(tab,p1):
    if(tab!=[]):
        if(len(tab) == 1):
            return 0
        j = 0
        p = tab[0]
        for i in range(0,len(tab)):
            if(plus_proche_nombre(p,tab[i],p1) == 2):
                j = i
                p = tab[i]
        return j
    
'''
    creer un tableau qui contient les tableaux contenant les points les plus proches des barycentres tabcluster  
'''
def rangement(tab,tabcluster):
    temp = []
    for i in tabcluster:
        temp.append([])
        
    for j in tab:
        temp[indice_barycentre_plus_proche_tab(tabcluster, j)].append(j)
    return temp

def affichertabtab(tab):
    print("[")
    for line in tab:
        print("[")
        for i in line:
            print("(" + str(i.x) + "," + str(i.y) + ")")
        print("]")
    print("]")

def affichertab(tab):
    for line in tab:
        print("(" + str(line.x) + "," + str(line.y) + ")")
'''
    renvoie un tableau avec les barycentres de tous les cluster du tableau
'''    
def tabbarycentre(tab):
    temp = []
    for line in tab:
        if line == []:
            return []
        bary = barycentre(line, len(line))
        temp.append(bary)
    return temp

def notequal(tab,tab1):
    if len(tab) != len(tab1):
        return -1
    for i in range(0,len(tab)):
        if tab[i].x != tab1[i].x or tab[i].y != tab1[i].y:
            return 1
    return 0

'''
    k = nb cluster a creer
    tab = tableau simple des points
'''
def KMeans(tab,k):
    tempbar = []
    tempbar.append(tab[0])
    for i in range(1,k):
        tempbar.append(tab[i])
    tabcluster = rangement(tab, tempbar)
    tempbarold = tempbar[:]
    tempbar = tabbarycentre(tabcluster)
   
    while notequal(tempbar,tempbarold) == 1:
         
        tabcluster = rangement(tab, tempbar)
        tempbarold = tempbar[:]
        tempbar = tabbarycentre(tabcluster)
            
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
def normalisation(tab):
    temp=[]
    col0=[]
    col1=[]
    for line in tab:
        col0.append(float(line[0]))
        col1.append(float(line[1]))
    col0n = normalisationcolonne(col0)
    col1n = normalisationcolonne(col1) 
    
    for i in range(0,len(col0n)):
        tempt = []
        tempt.append(col0n[i])
        tempt.append(col1n[i])
        temp.append(tempt)
    return temp    
'''
    parametre : tableau de Kmeans entierement trie, n en pourcentage
    retourne un tableau avec n% des extremite en moins
'''
            
def cluster_range(tab):
    bary = barycentre(tab,len(tab))
    temp = []
    i = 0
    for line in tab:
        temp2 = []
        d = distance(bary, line)
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

def moyenneseul(tab):
    return sum(tab, 0.0) / len(tab)
 
def varianceseul(tab):
    m=moyenneseul(tab)
    return moyenneseul([(x-m)**2 for x in tab])
 
def ecartypeseul(tab):
    return varianceseul(tab)**0.5
 
def ecartype(tab,numcol):
    return ecartypeseul(tab[numcol])
        

if __name__ == '__main__':
    print("Hello main method")
    
    dataset = load_csv()
    save_csv(dataset)
    cols = [18,2]
    tabfiltre = filtrage(dataset, cols)
    tabnormalise = normalisation(tabfiltre)
    moy = moyennecol(tabnormalise, 1)
    
    tabpoints = (transformer2(tabnormalise))
    #affichertab(newtab3)
    tabcluster = KMeans(tabpoints, 2)
    affichertabtab(tabcluster)
    
    #affichertab(barycentre(tabcluster))
    #affichertabtab(tab_cluster_range(tabcluster))
    #affichertab(extraction(tabcluster, 100))
    #afficher(dataset)
    #affichertabtab(KMeans(newtab3,2))
    
    
    
    