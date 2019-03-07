import tkinter as tk
import numpy as np
import pandas as py
import requests as rs
import re
from bs4 import BeautifulSoup
from tkinter import *
class SubWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Count Number of Tags")
        self.geometry("400x300+30+30")
        # Change what happens when you click the X button
        # This is done so changes also reflect in the main window class
        self.protocol('WM_DELETE_WINDOW', master.close)
        tk.Label(self,text="Enter the Website:").pack()
        
        tag_entry=tk.Entry(self,bd=5)
        tag_entry.pack()
        
       
        tk.Button(self,text="Click",command=lambda: self.calculate_tags(tag_entry.get())).pack()

        #tk.Button(self, text = "Print", command = self.printMessage).pack()

    def calculate_tags(self,line):      
        
        input_website=str(line)
        web="http://"+input_website
        response=rs.get(web)
        html=response.content
        soup=BeautifulSoup(html,'html.parser')
        image=soup.find_all('img')
        count_img=0
        for x in image:
            count_img=count_img+1
        print("Number of images :"+str(count_img))
        tk.Label(self,text="Number of Images:").pack()
        
        tag_image=tk.Entry(self,bd=5)
        tag_image.pack()
        tag_image.insert(0,str(count_img))
        links=soup.find_all("a")
        count_link=0
        for i in links:
            count_link=count_link+1
        print("Number of links:"+str(count_link))
        tk.Label(self,text="Number of Links:").pack()
        
        tag_link=tk.Entry(self,bd=5)
        tag_link.pack()
        tag_link.insert(0,str(count_link))             
        tb=soup.find_all("table")
        count_table=0
        for j in tb:
            count_table=count_table+1
        print("Number of tables:"+str(count_table)) 
        tk.Label(self,text="Number of tables:").pack()
        
        tag_table=tk.Entry(self,bd=5)
        tag_table.pack()
        tag_table.insert(0,str(count_table))
        div=soup.find_all("div")
        count_div=0
        for k in div:
            count_div=count_div+1
        print("Number of div:"+str(count_div))  
        tk.Label(self,text="Number of div:").pack()
        
        tag_div=tk.Entry(self,bd=5)
        tag_div.pack()
        tag_div.insert(0,str(count_div))
        header=soup.find_all("th")
        count_header=0
        for y in header:
            count_header=count_header+1
        print("Number of headers:"+str(count_header))  
        tk.Label(self,text="Number of header:").pack()
        
        tag_header=tk.Entry(self,bd=5)
        tag_header.pack()
        tag_header.insert(0,str(count_header))
             

        
        
        