import tkinter as tk
from tkinter.colorchooser import askcolor
from tkinter import *

effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}
aken = tk.Tk()

scales = 3

aken.title('Klahvistik')

akna_laius =700
akna_kõrgus = 400

ekraani_laius = aken.winfo_screenwidth()
ekraani_kõrgus = aken.winfo_screenheight()

keskelx = int(ekraani_laius / 2 - akna_laius / 2)
keskely = int(ekraani_kõrgus / 2 - akna_kõrgus / 2)

aken.geometry(f'{akna_laius}x{akna_kõrgus}+{keskelx}+{keskely}')

aken.resizable(False, False)
aken.attributes('-topmost', 1)

valge = 7
must = [1,1,0,1,1,1,0] * scales

for i in range(valge):
    tk.Button(aken, bg='White' , command=lambda i=i: clicked('White', i)).grid(row=0, column=i*3, rowspan=2, columnspan=3, ipadx=100, ipady=190, sticky='nsew')

for i in range(valge - 1):
    if must[i]:
        tk.Button(aken, bg='black', command=lambda i=i: clicked('Black',i)).grid(row=0, column=(i*3)+2, rowspan=1, columnspan=2, ipadx=30, ipady=120, sticky='n')
for i in range(valge*3):
    aken.columnconfigure(i, weight=1)



menüü = Menu(aken)
aken.config(menu=menüü)

faili_menüü = Menu(menüü)

faili_menüü.add_command(
    label='Exit',
    command=aken.destroy
)


def muuda_värvi():
    värvid = askcolor(title='Klahvistik')
    aken.configure(bg=värvid[1])


faili_menüü.add_command(
    label='Vali värv',
    command=muuda_värvi)

menüü.add_cascade(
    label='Fail',
    menu=faili_menüü
)

#7 valget + 5 musta klahvi on vaja (1 oktav)





aken.mainloop()
