import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

## OVDE DEFINISEMO PRVO PROZOR
window = Tk()
window.title("First Personal Application")
window.geometry("500x500")

## OVDE DEFINISEM GENERATOR KOJI KADA UKUCAM NESTO U ENTRY-JU VRATI MI U FAZONU POZDRAV TA I TA OSOBO
def Phrase_Generator():
    lista_fraza = ["Aloha ","Nice to meet you ","Good day ","Hello ","Zdravo ","Hafa adai "]
    rec = str(entry1.get())
    return lista_fraza[random.randint(0,5)] + rec


## OVA FUNKCIJA MI SLUZI ZA ISPIS
def Phrase_Display():
    pozdrav = Phrase_Generator()
    pozdrav_display = Text(master = window, height=6,width=30)
    pozdrav_display.grid(column=0, row=3)
    pozdrav_display.insert(END, pozdrav+"!")

## PRVA LABELA SA TEXTOM
label1 = Label(text="My first application! Welcome human.")
label1.grid(column=0,row=0,)

##DRUGA LABELA SA TEXTOM
label2 = Label(text="What's your name human?")
label2.grid(column=0,row=1,)

##PRAVIM ENTRY
entry1 = Entry()
entry1.grid(column=1,row=1)

##PRAVIM BUTTON(TASTER)
button1 = Button(text="Click meee!!!",command=Phrase_Display)
button1.grid(column=0,row=2)

##PRAVI PROZOR I TAKO I DA OSTANE, UVEK NA KRAJU IDE
window.mainloop()