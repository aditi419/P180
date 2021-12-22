from tkinter import *
from tkinter import ttk 
from googletrans import Translator
root = Tk()
root.geometry('800x600')
root.config(bg='lightgreen')

label_title = Label(root,text='LANGUAGE TRANSLATOR',bg='lightgreen',font=('Sylfean',30,'bold')) 
label_title.place(relx=0.5,rely=0.1,anchor=CENTER)

label = Label(root,text='Enter Text',bg='lightgreen',font=('Sylfean',20))
label.place(relx=0.19,rely=0.3,anchor=W)

textarea = Text(root,bg='lightgreen',font=('Sylfean',20),height=10,wrap='word',width=25,padx=2,pady=2,bd=0)
textarea.place(relx=0.25,rely=0.55,anchor=CENTER)

root.mainloop()