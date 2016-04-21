'''
Created on 15 avr. 2016

@author: tarek
'''
import csv
from Point.Point import Point
from math import sqrt

def afficher(tab):
    for line in tab:
        print(line)
'''
    filtre le dataset en nb de colonne indique dans un tableau
    renvoie un tableau avec les n colonnes choisies
'''
def filtrage(tab,tabcoldemande):
    temp = []
    for line in tab:
        temp2 =[]
        for numcol in tabcoldemande:
            temp2.append(line[numcol])
        temp.append(temp2)
    return temp
'''
    transforme un tableau de colonne du dataset en tableau de point 2D
'''
def transformer2(tab):
    temp = []
    for line in tab:
        temp.append(Point(float(line[0]),float(line[1]),int(line[2])))
    return temp

def transformer3(tab):
    temp = []
    for line in tab:
        temp.append(Point(float(line[0]),float(line[1]),float(line[2]),int(line[3])))
    return temp

def load_csv():
    spam_file="spambase.data"
    spam_data=open(spam_file,'r')
    data = csv.reader(spam_data)
    temp=[]
    for line in data:
        temp.append(line)
    
    return temp

  