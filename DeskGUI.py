from tkinter import *
from tkinter import filedialog
from logic import *
from tkinter import messagebox
import time 

s = time.time()

root = Tk()
root.geometry("400x150+500+150")
bgc="#0085fa"
fgc="white"
root.resizable(False,False)

root.title("Standard image to braille conversion")
root.config(bg=bgc)

def li():
    filetype_ = [('Jpg Files', '*.jpg'),("All files", "*.*")]
    n =  filedialog.askopenfilenames(initialdir = "/",title = "Select file",filetypes = (("JPG files","*.jpg"),("all files","*.*")))
    n = list(n)
    x=1
    s=time.time()
    while len(n) != 0:
        t = n.pop(0)
        inccont(t,x)
        x+=1
    if x!=1:
        final = time.time()-s
        final_=round(final,2)
        messagebox.showinfo("Info", f"Process completed in {final_}")

wl=Label(root,fg=fgc,text="Click here to load the image",font=("",15),bg=bgc)
wl.place(x=60,y=25)

fpb=Button(root,text="Load",width=15,height=1,font=("Arial",10),bd=0,fg=bgc,bg=fgc,command=li)
fpb.place(x=120,y=75)


root.mainloop()

