# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 11:04:14 2021

@author: jose-
"""

import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import tkinter.scrolledtext as scrolledtext
def getExcel ():
    global df
    import_file_path = filedialog.askopenfilename()
    data = pd.read_excel (import_file_path)
    df = pd.DataFrame(data,columns=['No.','TIPO DE CONSEJO','CABECERA','MODALIDAD'])
#crear Vista
def counter():
    modalidades = ['INDIVIDUAL','AGRUPACION']
    text.delete('1.0',tk.END)
    for modalidad in modalidades:
        head = f'\n========= CONSEJO MODALIDAD {modalidad} =========\n\n'
        consejo = df[df.MODALIDAD == modalidad].groupby(['TIPO DE CONSEJO','CABECERA']).size()
        text.insert(tk.END, head + str(consejo))
    
if __name__ == '__main__':
    #ventana
    root= tk.Tk()
    root.title('Calculos Observadores Electorales')
    root.geometry("500x400")
    root.resizable(0,1)

    # Botones
    browseButton_Excel = tk.Button(text='Importar Excel', command=getExcel, bg='#E12181', fg='white', font=('helvetica', 12, 'bold'))
    browseButton_Excel.grid(column=0,row=0,sticky="we")
    count = tk.Button(text='Realizar conteo', command=counter, bg='#E12181', fg='white', font=('helvetica', 12, 'bold'))
    count.grid(column=1,row=0,sticky="we")
    #vista
    text = scrolledtext.ScrolledText(root, undo=True,x=500,y=400)
    text.grid(column=0,row=1,columnspan=3, sticky="we")
    #run
    root.mainloop()