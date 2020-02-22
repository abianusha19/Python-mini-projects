import tkinter
import random
from PIL import Image,ImageTk
from tkinter import messagebox

colors=['BLUE','YELLOW','RED','VIOLET','GREEN','PINK','ORANGE','BROWN','BLACK','WHITE','GREY']
score=0
timeleft=30

window=tkinter.Tk()
def startgame(event):
    global timeleft
    if timeleft==30:
        countdown()
    nextcolor()


def nextcolor():
    global timeleft
    global score
    if timeleft>0:
        entry.focus_set()
        if entry.get().lower()==colors[1].lower():
            score+=1
        entry.delete(0,tkinter.END)
        random.shuffle(colors)
        label.config(fg=str(colors[1]),text=str(colors[0]))
        scorelabel.config(text="Your score is : "+str(score))
        

def countdown():
    global timeleft
    if timeleft>0:
        timeleft-=1
        timeLeft.config(text="Time left is : "+str(timeleft))
        timeLeft.after(1000,countdown)
        if timeleft==0:
             messagebox.showinfo("Score","Your score is "+str(score))



window.title("Color Game ")
window.configure(bg='#F08080')
#window.geometry('1500x1400')
image=Image.open('color2.gif')
photo=ImageTk.PhotoImage(image)
wd=photo.width()
ht=photo.height()
'''l = tkinter.Label(window,image=photo)
l.image = photo # keep a reference!
l.pack()'''
#window.geometry("%dx%d+0+0"%(wd,ht))
canvas1=tkinter.Canvas(window,width=1000,height=950)
canvas1.pack()
#background=canvas1.create_image(0,0,anchor=tkinter.NW,image=photo)
l = tkinter.Label(canvas1,image=photo)
l.pack()



l1=tkinter.Label(l,text=" Enter the color in words Watch and play ",font=("arial 20 bold"))
l1.pack()
#canvas1.wm_attributes('-transparentcolor',l1['bg'])
l2=tkinter.Label(l,text=" Press Enter to Start the game ",font=("arial 20 bold"))
l2.pack()
timeLeft=tkinter.Label(l,text=" Timeleft "+str(timeleft),font=("arial 20 bold"))
timeLeft.pack()
scorelabel=tkinter.Label(l,text=" Your score is : "+str(score))
scorelabel.pack()
label=tkinter.Label(window,font=("arial 60 bold"))
label.pack()
entry=tkinter.Entry(l)

window.bind("<Return>",startgame)

entry.pack()
entry.focus_set()
window.mainloop()
