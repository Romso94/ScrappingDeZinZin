from encodings import utf_8
from gettext import find
from msilib.schema import ListView
from operator import le
import re
from tkinter.messagebox import NO
from xmlrpc.server import XMLRPCDocGenerator
from numpy import pad
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import numpy as np 


def urltotxt():
    url = f'http://www.senat.fr/senateurs/senatl.html'   #Adresse a changer
    response = requests.get(f"{url}")

    


    soup = BeautifulSoup(response.text, 'lxml')  
    rep = soup.findAll('ul',{'class':"list-type-03"})
    with open ("caca.txt","w",encoding="utf-8") as f:
        f.write(str(rep))

    SenateurToDico()


def SenateurToDico():
    ListSenateur= []
 
    with open('caca.txt','r') as f:
        list=[]
        list.append(f.readline())
        while f.readline()!="":
            list.append(f.readline())
        for element in list:
            if '<li><a href="/senateur/' in element:
                ListSenateur.append(element)
        list=[]
        for element in ListSenateur:
            list.append(element[12:])
        ListSenateur=[]

        for element in list:
            val = element.split('"')
            ListSenateur.append(val[1])
        
    Dico_Senateurs=[]
    i=0
    for element in ListSenateur:
        url = f'http://www.senat.fr/'   #Adresse a changer
        response = requests.get(f"{url}{element}")
        soup = BeautifulSoup(response.text, 'lxml')

        try:
            rep1 = soup.findAll('div',{'class':'picture'})
            rep2=soup.find('a',{'class':'link-color-01'})
            rep4=soup.find('ul',{'class':'list-type-03'})
        except:
            pass
        

        str(rep1)
        nom =str(rep1[0]).split("\n")
        nom = nom[1].split('"')
        nom = nom[1].split(",")
        region = nom[1]
        nom=nom[0][9:]
        departement=' '
        try:
            region = region.split("(")
            departement = region[0]
            region=region[1][:-1]
        except:
            pass
        
        try:
            mail = str(rep2).split('>')
            mail = mail[1][:-3]
        except:
            pass

        election=None
        try:
            election = str(rep4).split("<li>")
            election=election[1].split("</li>")
            election=election[0].split("\n")
            election=election[1]

        except:
            pass
        
        
        Dico_Senateurs.append({"Nom":nom,"Region":region,"Departement":departement,"Email":mail,"Date_Election":election})
        print(f"Senateur numéro {i} enregistré")
        i+=1
  
    return Dico_Senateurs


    

    


        

    
   
    # with open('Clients1.csv', 'w',encoding='utf-8') as csvfile: 
    #     writer = csv.DictWriter(csvfile, fieldnames = field_names) 
    #     writer.writeheader() 
    #     writer.writerows(Dico_client) 
    
    # df_new = pd.read_csv('Clients1.csv') 
  
    # GFG = pd.ExcelWriter('Clients1.xlsx') 
    # df_new.to_excel(GFG, index = False) 
  
    # GFG.save() 



# urltotxt()

    

    
SenateurToDico()






    
   





