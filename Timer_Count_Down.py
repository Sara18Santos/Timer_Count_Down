# Count Down Timer 
import time
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x200")
root.title("Timer Count Down")

# variables 
hora = StringVar
minuto = StringVar
segundo = StringVar

#Set 
hora.set("00")
minuto.set("00")
segundo.set("00")

#Entry class
horaEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=hora)
horaEntry.place(x=80, y=20)
minutoEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=minuto)
minutoEntry.place(x=1300, y=20)
segudoEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=segundo)
segudoEntry.place(x=180, y=20)

def sumbit():
    try: 
        temp = int(hora.get())*3600 + int(minuto.get())*60 + int(segundo.get())
    except:
        print("Please input the right value.")
    while temp > -1:
        mins, secs =  divmod(temp,60)  # divmod(firstvalue = temp//60, secondvalue = temp%60)
        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr : 50min: 0sec)


root,mainloop()