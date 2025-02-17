from tkinter import *
def Train():
    """GUI"""
    import tkinter as tk
    import numpy as np
    import pandas as pd
    # import gtts
    # from gtts import gTTS
    # import requests
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import LabelEncoder

    root = tk.Tk()
    

    root.geometry("800x750")
    root.title("Cyberattack Detection Using ML")
    root.configure(background="brown")
    Total_Fwd_Packets = tk.IntVar()
    Total_Backward_Packets = tk.IntVar()
    Down_Up_Ratio = tk.IntVar()
    act_data_pkt_fwd= tk.IntVar()
    min_seg_size_forward = tk.IntVar()
    # Label = tk.IntVar()
   
    
    #===================================================================================================================
    #msg="Do's Attack Detected.."
    # def sms_send():
    #     url="https://www.fast2sms.com/dev/bulk"
    #     params={
      
    #         "authorization":"jmIw5r8SpconV1gXsB4JqTNkfYOP37dRHC2QDWxAibMZKtElaFPdJYpjLumUxDKfNE6Z12rTlRX9SOHo",
    #         "sender_id":"SMSINI",
    #         "message":msg,
    #         "language":"english",
    #         "route":"p",
    #         "numbers":"7887865466"
    #     }
    #     rs=requests.get(url,params=params)
    
    def Detect():
        
        
        e1=Total_Fwd_Packets.get()
        print(e1)
        e2= Total_Backward_Packets.get()
        print(e2)
        e3= Down_Up_Ratio.get()
        print(e3)
        e4=act_data_pkt_fwd.get()
        print(e4)
        e5=min_seg_size_forward.get()
        print(e5)
        # e6=Label.get()
        # print(e6)
        
        #########################################################################################
        
        from joblib import dump ,load
        a1=load('F:/protech solutions 2023/23CP109-Cyberattack Detection/Cyberattack  Detection/attack_RandomForest.joblib')
        v= a1.predict([[e1,e2,e3,e4,e5]])
        print(v)
        if v[0]==1:
            print("DOs")
            # sms_send()
            yes = tk.Label(root,text="DOs Attack Detected",background="green",foreground="white",font=('times', 20, ' bold '),width=32)
            yes.place(x=200,y=500)
                     
        elif v[0]==0:
            print("BENIGN")
            no = tk.Label(root, text="BENIGN Attack Detected", background="green", foreground="white",font=('times', 20, ' bold '),width=32)
            no.place(x=200, y=500)
            
            
        elif v[0]==2:
            print("PortScan")
            no = tk.Label(root, text="PortScan Attack Detected", background="green", foreground="white",font=('times', 20, ' bold '),width=32)
            no.place(x=200, y=500)
            
        elif v[0]==3:
            print("Bot")
            no = tk.Label(root, text="Bot Attack Detected", background="green", foreground="white",font=('times', 20, ' bold '),width=32)
            no.place(x=200, y=500)
            
        elif v[0]==4:
            print("WebAttack")
            no = tk.Label(root, text="WebAttack Detected", background="green", foreground="white",font=('times', 20, ' bold '),width=32)
            no.place(x=200, y=500)
            
        elif v[0]==5:
            print("BruteForce")
            no = tk.Label(root, text="BruteForce Attack Detected", background="green", foreground="white",font=('times', 20, ' bold '),width=32)
            no.place(x=200, y=500)
            
        else:
            print("No Attack Detected")
            label_text = "No Attack Detected"
    
            
    
        

    l1=tk.Label(root,text="Total_Fwd_Packets",background="seashell2",font=('times', 20, ' bold '),width=20)
    l1.place(x=5,y=50)
    Total_Fwd_Packets=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Total_Fwd_Packets)
    Total_Fwd_Packets.place(x=400,y=50)

    l2=tk.Label(root,text="Total_Backward_Packets",background="seashell2",font=('times', 20, ' bold '),width=20)
    l2.place(x=5,y=100)
    Total_Backward_Packets=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Total_Backward_Packets)
    Total_Backward_Packets.place(x=400,y=100)
    
    l3=tk.Label(root,text="Down_Up_Ratio",background="seashell2",font=('times', 20, ' bold '),width=20)
    l3.place(x=5,y=150)
    Down_Up_Ratio=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Down_Up_Ratio)
    Down_Up_Ratio.place(x=400,y=160)
    
    l4=tk.Label(root,text="act_data_pkt_fwd",background="seashell2",font=('times', 20, ' bold '),width=20)
    l4.place(x=5,y=200)
    act_data_pkt_fwd=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=act_data_pkt_fwd)
    act_data_pkt_fwd.place(x=400,y=200)
    
    l5=tk.Label(root,text="min_seg_size_forward",background="seashell2",font=('times', 20, ' bold '),width=20)
    l5.place(x=5,y=250)
    min_seg_size_forward=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=min_seg_size_forward)
    min_seg_size_forward.place(x=400,y=250)
  
    # l6=tk.Label(root,text="Label",background="olive",font=('times', 20, ' bold '),width=20)
    # l6.place(x=5,y=300)
    # Label=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Label)
    # Label.place(x=400,y=300)

    

    
    
    button1 = tk.Button(root,text="Submit",command=Detect,font=('times', 20, ' bold '),width=10)
    button1.place(x=300,y=400)


    root.mainloop()

Train()