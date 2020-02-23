import requests
from datetime import datetime
import tkinter
from PIL import Image,ImageTk

class scoreget:
    def __init__(self):
        self.url_get_all_matches="https://cricapi.com/api/matches"
        self.get_score="https://cricapi.com/api/cricketScore"
        self.api_key="XMUkXoiBu1X43og1sXOqISgRSTT2"
        self.unique_id=""
    def get_unique_id(self,team1,team2):
        url_params={"apikey":self.api_key}
        resp=requests.get(self.url_get_all_matches,params=url_params)
        resp_dict=resp.json()
        
        find=0
        for i in resp_dict['matches']:
            if((i["team-1"]==team1 and i["team-2"]==team2) or (i["team-1"]==team2 and i["team-2"]==team1) and i["matchStarted"]):               
                print(i['team-1'],i['team-2'])
                todaysdate=datetime.today().strftime('%Y-%m-%d')
                if todaysdate==i['date'].split('T')[0]:
                    self.unique_id=i['unique_id']
                    find=1
                    break
        if find==0:
            self.unique_id=-1
        send_data=self.get_score_current(self.unique_id,team1,team2)
        print(send_data)
        scoreres.set(send_data)
    
    def get_score_current(self,unique_id,team1,team2):
        data=""
        if unique_id==-1:
            data="No Specified Match Today"
        else:
            uri_params={"apikey":self.api_key,"unique_id":unique_id}
            resp=requests.get(self.get_score,params=uri_params)
            data_json=resp.json()
            try:
                data="Here is the Score :\n"+data_json['stat']+"\n"+data_json['score']
            except KeyError as e:
                print(e)
        return data

window=tkinter.Tk()
team1=tkinter.StringVar()
team2=tkinter.StringVar()
scoreres=tkinter.StringVar()
window.geometry('753x500')
window.configure(bg='#F08080')
image=Image.open('cricket1.jpg')
photo=ImageTk.PhotoImage(image)
label1=tkinter.Label(window,text="Live Cricket Score",font=("arial 20 bold"),bg='black',fg='white')
label1.grid(row=0,column=1)
canvas1=tkinter.Canvas(window,width=753,height=500)
background=canvas1.create_image(0,0,anchor=tkinter.NW,image=photo)
canvas1.grid(row=1,column=0,rowspan=8,columnspan=5)
label2=label1=tkinter.Label(window,text="Team 1 : ",font=("arial 20 bold"),bg='black',fg='white')
label2.grid(row=3,column=0)
entry1=tkinter.Entry(window,textvariable=team1,bg='black',fg='white')
entry1.grid(row=3,column=2)
label3=label1=tkinter.Label(window,text="Team 2 : ",font=("arial 20 bold"),bg='black',fg='white')
label3.grid(row=4,column=0)
entry2=tkinter.Entry(window,textvariable=team2,bg='black',fg='white')
entry2.grid(row=4,column=2)
score=scoreget()
button1=tkinter.Button(window,text="Get Score",command=lambda :score.get_unique_id(team1.get(),team2.get()),bg='black',fg='white')
button1.grid(row=5,column=1)
label=tkinter.Label(window,textvariable=scoreres,bg='black',fg='white',font=("Helvetica", 10))
label.grid(row=6,column=1)

window.mainloop()

        
                    
        