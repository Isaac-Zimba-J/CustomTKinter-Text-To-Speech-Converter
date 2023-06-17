import os
import sys
import tkinter as tk 
import customtkinter as ctk 
import pyttsx3 
from PIL import Image, ImageTk




#Conversion of text to speech
def Speak(*args):
    
    engine = pyttsx3.init()
    engine.setProperty('rate',rate_var.get())
    engine.setProperty('volume',(slider_var.get()/10))
    print(slider_var.get())
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[radio_var.get()].id)
    engine.say(args)
    engine.runAndWait()
    # engine.stop()
    

#read the text from entry
def ReadText(Text):
    Speak(Text.get())


def SaveRecord(*args):
    engine = pyttsx3.init()
    engine.setProperty('rate',125)
    engine.setProperty('volume', 0.9)
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[radio_var.get()].id)
    engine.say(args)
    engine.save_to_file(args,'Saved Reads/read.mp3')
    engine.runAndWait()
    

def SaveText(Text):
    SaveRecord(Text.get())

def RadioButton():
    print("Radio Button toggled, current value :",radio_var.get())


def SliderEvent(value):
    print(value)
    
def StopRead():
    breakpoint
# #set system appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# #Application starts here
app = ctk.CTk()
app.geometry("880x640")
app.resizable(False,False)
app.title("READMY")

#Canva geometry
app.columnconfigure((0,1,2), weight=1)
app.rowconfigure((0,1,2,3), weight=1)

#title
L_Text = ctk.CTkLabel(app, text="READMY TEXTS", font=('',20))
L_Text.grid(pady=5,row=0, column=1,sticky="n",)


#textbox
Text = tk.StringVar(value="Some Text to read")
T_Texbox = ctk.CTkEntry(app, width=350, height=230, textvariable=Text)
T_Texbox.grid(row=0, column=1, sticky="ew",pady=15)

#button

L_Button = ctk.CTkButton(app, text="Read", hover_color='#d96d49',fg_color='#d0491c',command=lambda: ReadText(Text),font=('',16))
L_Button.grid(row=0, column=2,pady=40,padx=20, sticky='new')

L_Button1 = ctk.CTkButton(app, text="Read and Save", hover_color='#e7a48d',fg_color='#de7f60',command=lambda: SaveText(Text),font=('',16))
L_Button1.grid(row=0, column=2,pady=80,padx=20, sticky='new')

L_Button1 = ctk.CTkButton(app,hover_color='#b70d0d',fg_color='#e51111', text="Stop", font=('',16),command= lambda: StopRead)
L_Button1.grid(row=0, column=2,pady=120,padx=20, sticky='new')



#Voice
L_Voice = ctk.CTkLabel(app,font=('',20), text='Chose voice')
L_Voice.grid(row=1, column=1, sticky='nw', pady=50)

#radio buttons
radio_var = tk.IntVar()
Voice_Radio_F = ctk.CTkRadioButton(app,font=('',16), text='Female', command=RadioButton,variable=radio_var, value=1)
Voice_Radio_M = ctk.CTkRadioButton(app,font=('',16), text='Male',command=RadioButton, variable=radio_var, value=0)
Voice_Radio_F.grid(row=1, column=1, sticky='sw', pady=35, padx=10)
Voice_Radio_M.grid(row=1, column=1, sticky='sw', pady=5, padx=10)


#Volume
L_Volume = ctk.CTkLabel(app,font=('',16), text='Volume')
L_Volume.grid(row=2, column=1, sticky='nw', pady=40)


#actual valume
slider_var = tk.IntVar(0)
V_Slider = ctk.CTkSlider(app,from_=0, to=10,command=SliderEvent,variable=slider_var , height=20 ,corner_radius=5,width=350,)
V_Slider.grid(row=2, column=1, sticky='w')

#Rate
L_Rate = ctk.CTkLabel(app,font=('',16), text='Read Speed')
L_Rate.grid(row=2, column=2, sticky='nw', pady=40)


#Rating
rate_var = tk.IntVar(0)
R_Slider = ctk.CTkSlider(app,from_=0, to=500,command=SliderEvent, variable=rate_var,height=20 ,corner_radius=5,width=350,)
R_Slider.grid(row=2, column=2, sticky='w')

R_Slider_Label = ctk.CTkLabel(app, text=R_Slider.get())



#image
logo = Image.open('images/logo1.png').resize((400,100))
test = ImageTk.PhotoImage(logo)

label1 = tk.Label(border=0, image=test)
label1.image = test
label1.grid(row=1,column=2, sticky='n')





app.mainloop()

