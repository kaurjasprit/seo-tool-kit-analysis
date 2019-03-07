import tkinter as tk
import numpy as np
import pandas as py
import requests as rs
import re
from bs4 import BeautifulSoup

class SubWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Count Number of Tags")
        self.geometry("400x300+30+30")
        # Change what happens when you click the X button
        # This is done so changes also reflect in the main window class
        self.protocol('WM_DELETE_WINDOW', master.close)
        tk.Label(self,text="Enter the Website:").pack()
        
        text_entry=tk.Entry(self,bd=5)
        text_entry.pack()
        
       
        tk.Button(self,text="Click",command=lambda: self.calculate_text(text_entry.get())).pack()
        
     
    def calculate_text(self,line):      
        
        input_website=str(line)
        web="http://"+input_website
        response=rs.get(web)
        html=response.content
        soup=BeautifulSoup(html,'html.parser') 
        count_text=0
        txt=soup.get_text()
        for t in txt:
               count_text=count_text+1
        print(count_text)       
        tk.Label(self,text="Number of Text:").pack()  
        key_word=tk.Entry(self,bd=5)
        key_word.pack()
        key_word.insert(0,str(count_text))
