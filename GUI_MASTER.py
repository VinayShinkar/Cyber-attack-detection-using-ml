from subprocess import call
import tkinter as tk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.tree import DecisionTreeClassifier 
from sklearn.ensemble import RandomForestClassifier  # Import Random Forest Classifier
from joblib import dump
import xgboost as xgb
from sklearn.naive_bayes import MultinomialNB 
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
root = tk.Tk()
root.title("Cyberattack Detection Using ML")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.configure(background="black")

image = Image.open('m4.jpg')

image = image.resize((1250,750), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image)

background_image=ImageTk.PhotoImage(image)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=70) #, relwidth=1, relheight=1)


image = Image.open('reg.jpg')

image = image.resize((270,620), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image)

background_image=ImageTk.PhotoImage(image)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=1260, y=70) 
# function to change to next image
# function to change to next image
'''def move():
	global x
	if x == 4:
		x = 1
	if x == 1:
		logo_label.config(image=img3)
	elif x == 2:
		logo_label.config(image=img2)
	elif x == 3:
		logo_label.config(image=img3)
	x = x+1
	root.after(2000, move)

# calling the function
move()'''




  # , relwidth=1, relheight=1)
lbl = tk.Label(root, text="Cyberattack Detection Using ML", font=('times', 35,' bold '), height=1, width=62,bg="brown",fg="white")
lbl.place(x=0, y=0)
# _+++++++++++++++++++++++++++++++++++++++++++++++++++++++

def Model_Training():
    data = pd.read_csv("test.csv")
    data.head()

    data = data.dropna()

   

    """Feature Selection => Manual"""
    x = data.drop(['Average_Packet_Size','Duration','Label'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['Label']
    print(type(y))
    x.shape
    

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30,random_state=123)

    # from sklearn.svm import SVC
    # svcclassifier = SVC(kernel='linear')
    # svcclassifier.fit(x_train, y_train)
    
    from sklearn.svm import SVC
    svcclassifier = SVC(kernel='linear')
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)

    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    label4 = tk.Label(root,text =str(repo),width=45,height=15,bg='seashell2',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=250,y=100)
    
    label5 = tk.Label(root,text ="Accuracy : "+str(ACC)+"%\nModel saved as attack_SVM.joblib",width=45,height=2,bg='black',fg='white',font=("Tempus Sanc ITC",14))
    label5.place(x=250,y=420)
    from joblib import dump
    dump (svcclassifier,"attack_SVM.joblib")
    print("Model saved as attack_SVM.joblib")

def Model_Training1():
    data = pd.read_csv("test.csv")
    data.head()

    data = data.dropna()

    """Feature Selection => Manual"""
    x = data.drop(['Average_Packet_Size', 'Duration','Label'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['Label']
    print(type(y))
    x.shape

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=123)

    # Replace SVM with Random Forest Classifier
    random_forest_classifier = RandomForestClassifier(n_estimators=100, random_state=123)
    random_forest_classifier.fit(x_train, y_train)

    y_pred = random_forest_classifier.predict(x_test)
    print(y_pred)

    print("=" * 40)
    print("==========")
    print("Classification Report : ", classification_report(y_test, y_pred))
    print("Accuracy : ", accuracy_score(y_test, y_pred) * 100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))

    label4 = tk.Label(root, text=str(repo), width=45, height=15, bg='seashell2', fg='black', font=("Tempus Sanc ITC", 14))
    label4.place(x=250, y=100)

    label5 = tk.Label(root,
                      text="Accuracy : " + str(ACC) + "%\nModel saved as attack_RandomForest.joblib",
                      width=45, height=2, bg='black', fg='white', font=("Tempus Sanc ITC", 14))
    label5.place(x=250, y=420)

    dump(random_forest_classifier, "attack_RandomForest.joblib")
    print("Model saved as attack_RandomForest.joblib")

def Model_Training2():
    data = pd.read_csv("test.csv")
    data.head()

    data = data.dropna()

    """Feature Selection => Manual"""
    x = data.drop(['Average_Packet_Size', 'Duration','Label'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['Label']
    print(type(y))
    x.shape

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=123)

    # Replace SVM with Decision Tree Classifier
    decision_tree_classifier = DecisionTreeClassifier(random_state=123)
    decision_tree_classifier.fit(x_train, y_train)

    y_pred = decision_tree_classifier.predict(x_test)
    print(y_pred)

    print("=" * 40)
    print("==========")
    print("Classification Report : ", classification_report(y_test, y_pred))
    print("Accuracy : ", accuracy_score(y_test, y_pred) * 100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))

    label4 = tk.Label(root, text=str(repo), width=45, height=15, bg='seashell2', fg='black', font=("Tempus Sanc ITC", 14))
    label4.place(x=250, y=100)

    label5 = tk.Label(root,
                      text="Accuracy : " + str(ACC) + "%\nModel saved as attack_DecisionTree.joblib",
                      width=45, height=2, bg='black', fg='white', font=("Tempus Sanc ITC", 14))
    label5.place(x=250, y=420)

    dump(decision_tree_classifier, "attack_DecisionTree.joblib")
    print("Model saved as attack_DecisionTree.joblib")

def Model_Training3():
    data = pd.read_csv("test.csv")
    data.head()

    data = data.dropna()

    """Feature Selection => Manual"""
    x = data.drop(['Average_Packet_Size', 'Duration','Label'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['Label']
    print(type(y))
    x.shape

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=123)

    # Replace SVM with Multinomial Naive Bayes Classifier
    naive_bayes_classifier = MultinomialNB()
    naive_bayes_classifier.fit(x_train, y_train)

    y_pred = naive_bayes_classifier.predict(x_test)
    print(y_pred)

    print("=" * 40)
    print("==========")
    print("Classification Report : ", classification_report(y_test, y_pred))
    print("Accuracy : ", accuracy_score(y_test, y_pred) * 100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))

    label4 = tk.Label(root, text=str(repo), width=45, height=15, bg='seashell2', fg='black', font=("Tempus Sanc ITC", 14))
    label4.place(x=250, y=100)

    label5 = tk.Label(root,
                      text="Accuracy : " + str(ACC) + "%\nModel saved as attack_NaiveBayes.joblib",
                      width=45, height=2, bg='black', fg='white', font=("Tempus Sanc ITC", 14))
    label5.place(x=250, y=420)

    dump(naive_bayes_classifier, "attack_NaiveBayes.joblib")
    print("Model saved as attack_NaiveBayes.joblib")

def Model_Training4():
    data = pd.read_csv("test.csv")
    data.head()

    data = data.dropna()

    """Feature Selection => Manual"""
    x = data.drop(['Average_Packet_Size', 'Duration','Label'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['Label']
    print(type(y))
    x.shape

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=123)

    # Replace SVM with XGBoost Classifier
    xgboost_classifier = xgb.XGBClassifier()
    xgboost_classifier.fit(x_train, y_train)

    y_pred = xgboost_classifier.predict(x_test)
    print(y_pred)

    print("=" * 40)
    print("==========")
    print("Classification Report : ", classification_report(y_test, y_pred))
    print("Accuracy : ", accuracy_score(y_test, y_pred) * 100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))

    label4 = tk.Label(root, text=str(repo), width=45, height=15, bg='seashell2', fg='black', font=("Tempus Sanc ITC", 14))
    label4.place(x=250, y=100)

    label5 = tk.Label(root,
                      text="Accuracy : " + str(ACC) + "%\nModel saved as attack_XGBoost.joblib",
                      width=45, height=2, bg='black', fg='white', font=("Tempus Sanc ITC", 14))
    label5.place(x=250, y=420)

    dump(xgboost_classifier, "attack_XGBoost.joblib")
    print("Model saved as attack_XGBoost.joblib")   
def call_file():
    from subprocess import call
    call(['python','Check.py'])
    #import Check.py
    #Check.py()




def window():
    root.destroy()

# button2 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
#                     text="Data_Preprocessing", command=Data_Preprocessing, width=15, height=2)
# button2.place(x=5, y=120)

button3 = tk.Button(root, foreground="white", background="#560319", font=("Tempus Sans ITC", 14, "bold"),
                    text="Model_SVM", command=Model_Training, width=15, height=2)
button3.place(x=1305, y=100)

button3 = tk.Button(root, foreground="white", background="#560319", font=("Tempus Sans ITC", 14, "bold"),
                    text="Model_RF", command=Model_Training1, width=15, height=2)
button3.place(x=1305, y=200)

button3 = tk.Button(root, foreground="white", background="#560319", font=("Tempus Sans ITC", 14, "bold"),
                    text="Model_DT", command=Model_Training2, width=15, height=2)
button3.place(x=1305, y=300)

# +

button3 = tk.Button(root, foreground="white", background="#560319", font=("Tempus Sans ITC", 14, "bold"),
                    text="Model_NB", command=Model_Training3, width=15, height=2)
button3.place(x=1305, y=400)

# +

button3 = tk.Button(root, foreground="white", background="#560319", font=("Tempus Sans ITC", 14, "bold"),
                    text="Model_xgboost", command=Model_Training4, width=15, height=2)
button3.place(x=1305, y=500)

# +






0button4 = tk.Button(root, foreground="white", background="#560319", font=("Tempus Sans ITC", 14, "bold"),
                    text="Check Performance", command=call_file, width=15, height=2)
button4.place(x=1305, y=600)
exit = tk.Button(root, text="Exit", command=window, width=15, height=2, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=1305, y=720)
# -

root.mainloop()

'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''











# +



# -



























































