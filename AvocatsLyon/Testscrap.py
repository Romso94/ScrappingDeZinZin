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





def BarreauToDico(i):
    Dico_client = []
    while i<335:
        url = f'https://www.barreaulyon.com/annuaire?paged={i}'   #Adresse a changer
        response = requests.get(f"{url}")


        soup = BeautifulSoup(response.text, 'lxml')  
        rep = soup.findAll('div',{'class':'entry-content'})

        

        
        
        Liste =[]

        for element in rep:
            
            Liste.append(str(element))

        print(f'Page {i}')

        for element in Liste:

            val = element.split("\n")

    
            
            if len(val)==10:
                try:
                    nom = val[3].split('>')
                    nom = nom[1].split('  ')
                    Nom = nom[0]

                    numero = val[7].split('>')
                    numero = numero[1].split('<')
                    Numero = numero[0]

                    Dico_client.append({'Nom':Nom,'Numero':Numero,'Mail':' ','Entreprise':' ','Site':' '})
                except:
                    pass
                


            if len(val)==14:
                try:
                    nom = val[3].split('>')
                    nom = nom[1].split('  ')
                    Nom = nom[0]

                    mail = val[7].split('>')
                    mail = mail[1].split('<')
                    Mail = mail[0]

                    numero = val[11].split('>')
                    numero = numero[1].split('<')
                    Numero = numero[0]

                    Dico_client.append({'Nom':Nom,'Numero':Numero,'Mail':Mail,'Entreprise':' ','Site':' '})
                    
                
                except:
                    pass

            
            

            if len(val)==18:
                try:
                    nom_entreprise = val[1].split('>')
                    Nom_entreprise = nom_entreprise[1].split('  ')
                    Nom_entreprise = Nom_entreprise[0]

                    nom = val[3].split('>')
                    nom = nom[1].split('  ')
                    Nom = nom[0]
                    
                    
                    mail = val[7].split('>')
                    mail = mail[1].split('<')
                    Mail = mail[0]

                    numero = val[11].split('>')
                    numero = numero[1].split('<')
                    Numero = numero[0]

                    
                    Dico_client.append({'Nom':Nom,'Numero':Numero,'Mail':Mail,'Entreprise':Nom_entreprise,'Site':' '})
                   
                
                except:
                    pass

            if len(val)==22:
                try:
                    nom_entreprise = val[1].split('>')
                    Nom_entreprise = nom_entreprise[1].split('  ')
                    Nom_entreprise = Nom_entreprise[0]

                    nom = val[3].split('>')
                    nom = nom[1].split('  ')
                    Nom = nom[0]
                    
                    mail = val[7].split('>')
                    mail = mail[1].split('<')
                    Mail = mail[0]

                    numero = val[11].split('>')
                    numero = numero[1].split('<')
                    Numero = numero[0]

                    site = val[15].split('>')
                    site = site[1].split(' ')
                    Site  = site[0]
                    
                    

                    Dico_client.append({'Nom':Nom,'Numero':Numero,'Mail':Mail,'Entreprise':Nom_entreprise, 'Site':Site})
                  
            
                except:
                    pass
        i+=1

    field_names = ['Nom','Numero','Mail','Entreprise','Site'] 
    
   
    with open('Clients1.csv', 'w',encoding='utf-8') as csvfile: 
        writer = csv.DictWriter(csvfile, fieldnames = field_names) 
        writer.writeheader() 
        writer.writerows(Dico_client) 
    
    df_new = pd.read_csv('Clients1.csv') 
  
    GFG = pd.ExcelWriter('Clients1.xlsx') 
    df_new.to_excel(GFG, index = False) 
  
    GFG.save() 



    

    
BarreauToDico(1)






    
   





