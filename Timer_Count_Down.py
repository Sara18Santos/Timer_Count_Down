# Count Down Timer 
import time
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x250")
root.title("Timer Count Down")

# variables 
hora = StringVar()
minuto = StringVar()
segundo = StringVar()

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
        horas = 0
        if mins > 60:
            horas, mins = divmod(mins, 60)
        # store the value up to two decimal places
        hora.set("{0:2d}".format(hours))
        minuto.set("{0:2d}".format(mins))
        segundo.set("{0:2d}".format(secs))

        # Update the GUI window after decrementing the temp value every time
        root.update()
        time.sleep(1)

        #When temp  value = 0, then messagebox pop's up
        if (temp == 0):
            messagebox.showinfo("Time CountDown", "Time's up")
        # after every one sec the value of temp wil be decremented by one
        temp -=1

# Button 
btn_start = Button(root, text="Set Time Countdown", bd='5', command=submit)
btn.place(x=70, y=120)

root.mainloop()