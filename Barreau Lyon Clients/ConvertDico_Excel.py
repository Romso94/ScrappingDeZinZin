from Testscrap import BarreauToDico
import pandas as pd
import csv
import numpy as np 

def DicoToExcel (Dico):

    field_names = ['Nom','Numero','Mail','Entreprise','Site'] 
    
    
    with open('Clients1.csv', 'w',encoding='utf-8') as csvfile: 
        writer = csv.DictWriter(csvfile, fieldnames = field_names) 
        writer.writeheader() 
        writer.writerows(Dico) 
    
    df_new = pd.read_csv('Clients1.csv') 
  
    GFG = pd.ExcelWriter('Clients1.xlsx') 
    df_new.to_excel(GFG, index = False) 
  
    GFG.save() 
    



DicoToExcel(BarreauToDico(1))

