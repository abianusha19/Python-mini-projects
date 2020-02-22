import tkinter
from time import strftime 
  
window=tkinter.Tk()
window.title("Digital Clock")
def time(): 
    string = strftime('%H:%M:%S %p') 
    lbl.config(text = string) 
    lbl.after(1000, time) 
lbl = tkinter.Label(window, font = ('calibri', 40, 'bold'), 
            background = 'Black', 
            foreground = 'Red') 
lbl.pack(anchor = 'center') 
time() 
  
window.mainloop() 
