# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 11:04:14 2021

@author: jose-
"""

import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

root= tk.Tk()
root.title('Calculos Consejos')


def getExcel ():
    global df
    import_file_path = filedialog.askopenfilename()
    data = pd.read_excel (import_file_path)
    df = pd.DataFrame(data,columns=['No.','TIPO DE CONSEJO','CABECERA','MODALIDAD'])
    global consejos
    consejos = df[df.MODALIDAD == 'INDIVIDUAL'].groupby(['TIPO DE CONSEJO','CABECERA']).size()

#crear Vista
def counter():
     text.insert(tk.END, str(consejos))
    
    
    
# Botones
browseButton_Excel = tk.Button(text='Importar Excel', command=getExcel, bg='#E12181', fg='white', font=('helvetica', 12, 'bold'))
count = tk.Button(text='Realizar conteo', command=counter, bg='#E12181', fg='white', font=('helvetica', 12, 'bold'))

browseButton_Excel.pack(side=tk.LEFT)
count.pack(side=tk.RIGHT)

#vista
text = tk.Text()
text.pack(side=tk.TOP);




root.mainloop()