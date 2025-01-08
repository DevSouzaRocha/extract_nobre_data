from extract_he import get_extra_hours
from extract_ho import get_ho
import numpy as np
import pandas as pd

he = get_extra_hours().set_index('Nome')
ho = get_ho().set_index('Nome')


frame = ho.join(he,lsuffix='_caller', rsuffix='_other',how='outer')

frame['Horas_60'].fillna('00:00',inplace=True)
frame[['H_60','M_60']] = frame['Horas_60'].astype(str).str.split(':',expand=True)

frame['Horas_100'].fillna('00:00',inplace=True)
frame[['H_100','M_100']] = frame['Horas_100'].astype(str).str.split(':',expand=True)

frame['Total_HE_60'] = (frame['H_60'].astype(float)  + frame['M_60'].astype(float)/60) *frame['Base'].astype(float)* 1.6
frame['Total_HE_100'] = (frame['H_100'].astype(float)  + frame['M_100'].astype(float)/60) *frame['Base'].astype(float)* 2

frame.fillna(0,inplace=True)
frame['Total'] = frame['Total_HE_60'] + frame['Total_HE_100'] + frame['Liquido']

print(frame)

frame.to_excel('output.xlsx')
