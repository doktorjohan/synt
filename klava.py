import tkinter as tk
from tkinter.colorchooser import askcolor
from tkinter import Menu



aken = tk.Tk()

aken.title('Klahvistik')

akna_laius = 800
akna_kõrgus = 400

ekraani_laius = aken.winfo_screenwidth()
ekraani_kõrgus = aken.winfo_screenheight()

keskelx = int(ekraani_laius / 2 - akna_laius / 2)
keskely = int(ekraani_kõrgus / 2 - akna_kõrgus / 2)

aken.geometry(f'{akna_laius}x{akna_kõrgus}+{keskelx}+{keskely}')

aken.resizable(False, False)
aken.attributes('-topmost', 1)

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

aken.mainloop()
