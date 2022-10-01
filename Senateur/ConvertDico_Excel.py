from Testscrap import  SenateurToDico
import pandas as pd
import csv
import numpy as np 

def DicoToExcel (Dico):



    field_names = ['Nom','Region','Departement','Email','Date_Election'] 
    
    
    with open('Senateurs.csv', 'w',encoding='utf-8') as csvfile: 
        writer = csv.DictWriter(csvfile, fieldnames = field_names) 
        writer.writeheader() 
        writer.writerows(Dico) 
    
    df_new = pd.read_csv('Senateurs.csv') 
  
    GFG = pd.ExcelWriter('Senateurs.xlsx') 
    df_new.to_excel(GFG, index = False) 
  
    GFG.save() 
    



DicoToExcel(SenateurToDico())

