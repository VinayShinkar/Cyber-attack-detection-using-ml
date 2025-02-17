  # -*- coding: utf-8 -*-
# +
"""
Created on Mon Jan 18 16:37:36 2021-=[]\p

@author: sheet
"""

pip install --upgrade pip
# -

import sqlite3
import tkinter  as tk 
from tkinter import * 
import time
import numpy as np


pip install --upgrade pillow

import os
from PIL import Image # For face recognition we will the the LBPH Face Recognizer 
from PIL import Image , ImageTk  

root = tk.Tk()
#root.geometry('500x500')
#root.title("Login Form")


# ------------------------------------------------------

root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Cyberattack Detection Using ML")
#------------------Frame----------------------



# -------function------------------------



# #### tkinter window ######

# +

def reg():
    print("reg")
    from subprocess import call
    call(["python", "registration.py"])   

# +




# -



#
# #### tkinter window ######

def login():
    print("log")
    from subprocess import call
    call(["python", "login.py"])   


# +
root = tk.Tk()
root.geometry("800x600")  # Set window size

# Define width and height for image resizing
w, h = 800, 600  

# Load background image safely
image_path = "C:/Users/Mahavir/Downloads/Cyberattack  Detection/Cyberattack  Detection/m4.jpg"

if os.path.exists(image_path):  
    image2 = Image.open(image_path)
    image2 = image2.resize((w, h), Image.Resampling.LANCZOS)  
    root.background_image = ImageTk.PhotoImage(image2)  # Store reference
else:
    print(f"Error: File '{image_path}' not found.")
    root.background_image = None  

if root.background_image:
    background_label = tk.Label(root, image=root.background_image)
    background_label.place(x=0, y=0)  # Place background

# Title label
lbl = tk.Label(root, text="Cyberattack Detection Using ML",
               font=('times', 40, 'bold'), height=1, width=50,
               bg="brown", fg="white")
lbl.place(x=0, y=5)

# Frame
framed = tk.LabelFrame(root, text=" --WELCOME-- ", width=500, height=210,
                       bd=5, font=('times', 14, 'bold'), bg="pink")
framed.place(x=20, y=90)  # Removed .grid()

root.mainloop()


# + +++++++++++++++++++++++++++++++++++++++++++
#####For background Image
button1 = tk.Button(framed, text='Login Now',width=15,height=2,bg='dark blue',fg='white',command=login,font='bold').place(x=30,y=65)
button1 = tk.Button(framed, text='Register',width=15,height=2,bg='dark blue',fg='white',command=reg,font='bold').place(x=250,y=65)

""
root.mainloop()
# -

pip install Pillow



# +




# -

#

Image.Resampling.LANCZOS



# +









# +



# -







# +




# -











































