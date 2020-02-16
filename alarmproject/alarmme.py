import tkinter
import datetime
import beep
window=tkinter.Tk()
window.title("Alarm clock")
runTime=tkinter.StringVar()
waitingtime=tkinter.IntVar()
runTime.set(datetime.datetime.now())

alarmtime=None
def set_alarm():
    sec=waitingtime.get()
    global alarmtime
    alarmtime=datetime.datetime.now()+datetime.timedelta(seconds=sec)
    runTime.set(alarmtime)
    return
    
def destroy():
    return 

def regular_update():
    window.update()
    window.update_idletasks()
    global alarmtime
    if alarmtime:
        if datetime.datetime.now()>alarmtime:
            beep.beep(1)
            return 
l1=tkinter.Label(window,text="Alarm Time :",font=("arial 20 bold"))
l1.grid(row=0,column=1,columnspan=4,padx=10,pady=10)
l2=tkinter.Label(window,textvariable=runTime,font=("arial 20 bold"))
l2.grid(row=0,column=6,columnspan=4)
l3=tkinter.Label(window,text="Wait for seconds")
l3.grid(row=2,column=1,columnspan=4)
tb=tkinter.Entry(window,textvariable=waitingtime)
tb.grid(row=2,column=6,columnspan=4)
button1=tkinter.Button(window,text="Set Alarm!",command=set_alarm)
button1.grid(row=3,column=3,columnspan=4)
button2=tkinter.Button(window,text="exit",command=window.destroy)
button2.grid(row=3,column=5,columnspan=4)

def main():
    while True:
        regular_update()
    return
if __name__=='__main__':
    main()
window.mainloop()