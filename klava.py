import tkinter as tk
from tkinter.colorchooser import askcolor
from tkinter import *
import os
import main

note_dict = {
    "a": 261.63,
    "w": 277.18,
    "s": 293.66,
    "e": 311.13,
    "d": 329.63,
    "f": 349.23,
    "t": 369.99,
    "g": 392.00,
    "y": 415.30,
    "h": 440.0,
    "u": 466.16,
    "j": 493.88
}

selected_octave = 1

aken = tk.Tk()

scales = 3

aken.title('Klahvistik')

akna_laius = 700
akna_kõrgus = 400

ekraani_laius = aken.winfo_screenwidth()
ekraani_kõrgus = aken.winfo_screenheight()

keskelx = int(ekraani_laius / 2 - akna_laius / 2)
keskely = int(ekraani_kõrgus / 2 - akna_kõrgus / 2)

aken.geometry(f'{akna_laius}x{akna_kõrgus}+{keskelx}+{keskely}')

aken.resizable(False, False)
aken.attributes('-topmost', 1)

def clicked(color, num):
    print(color + ': '+str(num))
    main.sound_generator(note_dict[num.char], selected_octave)

def shift_octave_down():
    global selected_octave
    selected_octave /= 2

def shift_octave_up():
    global selected_octave
    selected_octave *= 2

oktav_alla = tk.Button(aken, text="-", command=shift_octave_down)
oktav_yles = tk.Button(aken, text='+', command=shift_octave_up)


valge = 7
must = [1, 1, 0, 1, 1, 1, 0] * scales
valged_klahvid = ['a','s','d','f','g','h','j']
mustad_klahvid = ['w','e','t','y','u']
o = 0


for i in range(valge):
    Button(aken, text=valged_klahvid[i], bg='White', command=lambda i=i: clicked('White', i)).grid(row=0, column=i*3, rowspan=2, columnspan=3, ipadx=100, ipady=190, sticky='nsew')
    aken.bind(valged_klahvid[i], lambda i=i: clicked('White', i))

for i in range(valge - 1):
    if must[i]:
        Button(aken, text=mustad_klahvid[o], bg='black', fg='white', command=lambda i=i: clicked('Black', i)).grid(row=0, column=(i*3)+2, rowspan=1, columnspan=2, ipadx=30, ipady=120, sticky='n')
        aken.bind(mustad_klahvid[o], lambda i=i: clicked('Black', i))
        o = o + 1

for i in range(valge*3):
    aken.columnconfigure(i, weight=1)

menüü = Menu(aken)
aken.config(menu=menüü)

faili_menüü = Menu(menüü)

faili_menüü.add_command(
    label='Exit',
    command=aken.destroy
)


oktav_menu = Menu(menüü)
oktav_menu.add_command(
    label='oktav üles',
    command=shift_octave_up
)

oktav_menu.add_command(
    label='oktav alla',
    command=shift_octave_down
)


def muuda_värvi():
    värvid = askcolor(title='Klahvistik')
    aken.configure(bg=värvid[1])


faili_menüü.add_command(
    label='Vali värv',
    command=muuda_värvi
)

menüü.add_cascade(
    label='Fail',
    menu=faili_menüü
)

menüü.add_cascade(
    label='Vali oktav',
    menu=oktav_menu
)

aken.mainloop()
