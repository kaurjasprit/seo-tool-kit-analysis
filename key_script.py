import tkinter as tk
import numpy as np
import pandas as py
import requests as rs
import re
from bs4 import BeautifulSoup

class SubWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Count Number of keywords")
        self.geometry("400x300+30+30")
        # Change what happens when you click the X button
        # This is done so changes also reflect in the main window class
        self.protocol('WM_DELETE_WINDOW', master.close)
        tk.Label(self,text="Enter the Website:").pack()
        
        web_entry=tk.Entry(self,bd=5)
        web_entry.pack()
        
        tk.Label(self,text="Enter the Keyword:").pack()
        key_entry=tk.Entry(self,bd=5)
        key_entry.pack()
        
       
        tk.Button(self,text="Click",command=lambda: self.calculate_keys(web_entry.get(),key_entry.get())).pack()
      
    def calculate_keys(self,lines,word):
        input_website=str(lines)
        web="http://"+input_website
        response=rs.get(web)
        html=response.content
        soup=BeautifulSoup(html,'html.parser')
        key_search=soup.find_all(string=re.compile(word,re.IGNORECASE))
        count_key=0
        for z in key_search:
                 count_key=count_key+1
        print(count_key)
        tk.Label(self,text="Number of Keywords:").pack()  
        key_word=tk.Entry(self,bd=5)
        key_word.pack()
        key_word.insert(0,str(count_key))
                     
        
        
        
