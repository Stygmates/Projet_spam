'''
Created on 15 avr. 2016

@author: tarek
'''
import csv


def save_csv(tab):
    spam_file="spamsave.csv"
    spam_data=open(spam_file,'w')
    spamwriter = csv.writer(spam_data, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for line in tab:
        spamwriter.writerow(line)
        
