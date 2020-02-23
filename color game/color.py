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

image=Image.open('color2.gif')
photo=ImageTk.PhotoImage(image)
wd=photo.width()
ht=photo.height()
window.geometry('896x500')
'''l = tkinter.Label(window,image=photo)
l.image = photo # keep a reference!
l.pack()'''
#window.geometry("%dx%d+0+0"%(wd,ht))
canvas1=tkinter.Canvas(window,width=896,height=500)
canvas1.grid(row=0,column=0,rowspan=8,columnspan=5)
background=canvas1.create_image(0,0,anchor=tkinter.NW,image=photo)



l1=tkinter.Label(window,text=" Enter the color in words Watch and play ",font=("arial 20 bold"),bg='pink',fg='black')
l1.grid(row=1,column=1)
#canvas1.wm_attributes('-transparentcolor',l1['bg'])
l2=tkinter.Label(window,text=" Press Enter to Start the game ",font=("arial 20 bold"),bg='pink',fg='black')
l2.grid(row=2,column=1)
timeLeft=tkinter.Label(window,text=" Timeleft "+str(timeleft),font=("arial 20 bold"),bg='pink',fg='black')
timeLeft.grid(row=3,column=1)
scorelabel=tkinter.Label(window,text=" Your score is : "+str(score),bg='pink',fg='black')
scorelabel.grid(row=4,column=1)
label=tkinter.Label(window,font=("arial 60 bold"))
label.grid(row=5,column=1)
entry=tkinter.Entry(window,bg='black',fg='white')

window.bind("<Return>",startgame)

entry.grid(row=6,column=1)
entry.focus_set()
window.mainloop()
