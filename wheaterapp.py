import json
import tkinter
import requests
from tkinter import *

def check():
    try:
        resp = requests.get(f"https://wttr.in/{city.get().capitalize()}?format=j1")
        wheather = resp.json()
        resault.configure(text=f"resault:{wheather['current_condition'][0]['temp_C']}C",fg="green")
    except:
        resault.configure(text=f"inter a valid city name",fg="red")

main = tkinter.Tk()
main.configure(width=300,height=300)
city = tkinter.Entry(width=200, master=main)
city.insert(0,"inter your city name")
city.place(x=1,y=1)
btn = tkinter.Button(master=main, text = "check", command=lambda:check())
btn.place(x=1,y=20)
resault = tkinter.Label(master=main, text="resault:")
resault.place(x=1,y=40)
main.mainloop()