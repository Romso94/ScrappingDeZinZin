
from encodings import utf_8
from gettext import find
from msilib.schema import ListView
from operator import le
from pickle import NONE
import re
import site
from tkinter import NE
from tkinter.messagebox import NO
from xmlrpc.server import XMLRPCDocGenerator
from numpy import pad
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import numpy as np 
import time


def urltotxt():
    url = f'https://www2.assemblee-nationale.fr/deputes/liste/alphabetique'   #Adresse a changer
    response = requests.get(f"{url}")

    


    soup = BeautifulSoup(response.text, 'lxml')  
    rep = soup.findAll('div',{'id':"deputes-list"})
    with open ("caca.txt","w",encoding="utf-8") as f:
        f.write(str(rep))




def DeputeToDico():
    ListDepute = []

    with open("caca.txt","r",encoding="utf-8") as f:
        list=[]
        list.append(f.readline())
        while f.readline()!="":
            list.append(f.readline())
        
        NewList=[]
        for element in list:
            if "/deputes/fiche/" in element:
                NewList.append(element)
        
        list= []
        for element in NewList:
            var = element.split('"')
            list.append(var[1])
        
    url = "https://www2.assemblee-nationale.fr/"
    for i in range(len(list)-1):
        response = requests.get(f"{url}{list[i]}")
        soup = BeautifulSoup(response.text, 'lxml')  
        
        try: 
            rep1 = soup.find('div',{'id':'deputes-illustration'})
            rep2 = soup.find('p',{'class':'deputy-healine-sub-title'})
            rep3 = soup.find('dl',{'class':'deputes-liste-attributs'})
            rep4 = soup.find('div',{'class':'titre-bandeau-bleu clearfix'})
        except:
            pass
        partipolitique=NONE
        Ville = NONE
        siteWeb = NONE
        Prenom = NONE
        mail = NONE 
        
        try:
            val = str(rep1).split('groupe">')
            partipolitique = val[-1][:-18]

            val = str(rep2).split('>')
            val = val[1].split("&")
            Ville = val[0]
        except:
            pass
        
        try:
            val = str(rep3).split('<a href="')
            siteWeb = val[4].split('"')
            siteWeb = siteWeb[0]
        except:
            pass
        try:
            val = str(rep3).split('<a href="')
            mail = val[3].split(">")
            mail = mail[1][:-3]
        except:
            pass

        try:
            val = str(rep4).split('h1')
            Prenom = val[1][:-2][1:]
        except:
            pass

        ListDepute.append({"Nom":Prenom,"Mail":mail,"Ville":Ville,"Parti_Politique":partipolitique,"Site_Internet":siteWeb})
        print(f"Depute {i} enregistré")
    
    
    return ListDepute


def DicoToExcel (Dico):

    field_names = ['Nom','Mail','Ville','Parti_Politique','Site_Internet'] 
    
    
    with open('Deputes.csv', 'w',encoding='utf-8') as csvfile: 
        writer = csv.DictWriter(csvfile, fieldnames = field_names) 
        writer.writeheader() 
        writer.writerows(Dico) 
    
    df_new = pd.read_csv('Deputes.csv') 
  
    GFG = pd.ExcelWriter('Deputes.xlsx') 
    df_new.to_excel(GFG, index = False) 
  
    GFG.save() 
    





DicoToExcel(DeputeToDico())


 
   


    

    


        

    
   
    # with open('Clients1.csv', 'w',encoding='utf-8') as csvfile: 
    #     writer = csv.DictWriter(csvfile, fieldnames = field_names) 
    #     writer.writeheader() 
    #     writer.writerows(Dico_client) 
    
    # df_new = pd.read_csv('Clients1.csv') 
  
    # GFG = pd.ExcelWriter('Clients1.xlsx') 
    # df_new.to_excel(GFG, index = False) 
  
    # GFG.save() 



# urltotxt()

    

    
