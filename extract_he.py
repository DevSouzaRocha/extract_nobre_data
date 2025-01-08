from tabula import read_pdf
import pandas as pd
import math
import glob
import os

def get_extra_hours():
    data = []
    #reads table from pdf file
    for i in range(1,100):
        try:
            list_of_files = glob.glob('he/*') # * means all if need specific format then *.csv
            latest_file = max(list_of_files, key=os.path.getctime)

            file_path = 'he'+'/'+latest_file.split('\\')[-1]
            #Getting tables
            df = read_pdf(file_path,pages=i,guess=False,lattice=True)
            #Getting employee name
            name = df[0].iloc[1,0]
            name = name.split(':')[1].strip()
            if df[2].shape[1] == 17:
                #Getting employee 60% extra work hours 
                horas_60x = '00:00'     
                #Getting employee 100% extra work hours 
                horas_100x = '00:00'
                data.append([name,horas_60x,horas_100x])
            elif df[2].shape[1] == 18:
                #Getting employee 60% extra work hours 
                horas_60x = df[2].iloc[-1,13]     
                #Getting employee 100% extra work hours 
                horas_100x = '00:00'
                data.append([name,horas_60x,horas_100x])
            elif df[2].shape[1] == 19:
                #Getting employee 60% extra work hours 
                horas_60x = df[2].iloc[-1,13]     
                #Getting employee 100% extra work hours 
                horas_100x = df[2].iloc[-1,14]
                data.append([name,horas_60x,horas_100x])
        except:
            print("An exception occurred")
        
    frame = pd.DataFrame(data=data,columns=['Nome','Horas_60','Horas_100'])
    frame.fillna(0,inplace=True)
    return frame