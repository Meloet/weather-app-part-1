from tkinter import *
from tkinter.font import BOLD
import requests

def getweather():
    city=city_text.get()
root=Tk()
root.title('Weather App')
root.geometry('500x300')

title=Label(root,text='Weather App',font=('bold',10)).place(x=190,y=50)
city_label=Label(root,text='Enter Your City',font=('bold',15)).place(x=110,y=80)
city_text=StringVar()
city_entry=Entry(root,textvariable=city_text)
city_entry.place(x=265,y=90)

goButton=Button(root,text='Go',width=12,command=getweather)
goButton.place(x=210,y=120)
root.mainloop()