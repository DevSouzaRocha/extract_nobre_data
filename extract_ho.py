from tabula import read_pdf
import pandas as pd
import os
 
 
def get_ho():
    
    
    for _, _, arquivos in os.walk('holerites'):
        
        data = []
        for arquivo in arquivos:
        #reads table from pdf file
            path = 'holerites'+'/' + arquivo
        
            df = read_pdf(path,stream=True, pages='all') #address of pdf file
            for i in df:
                #Getting employee name
                name = i.iloc[2,0]
                name = name.split(' ',1)[1]
                
                #Getting employee base salary
                base_salary = i.iloc[5,-1].replace('.','').replace(',','.')
                
                #Getting employee base salary
                row_index = i.index[i['RECIBO DE PAGAMENTO'].str.contains('Total Liquido') == True].tolist()[0]
                salary = i.iloc[row_index,-1].split(' ')[2].replace('.','').replace(',','.')
                data.append([name,float(base_salary)/220,float(salary)])

        frame = pd.DataFrame(data=data,columns=['Nome','Base','Liquido'])
        frame.drop_duplicates(inplace=True)
        return frame