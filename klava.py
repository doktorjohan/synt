import tkinter as tk
aken = tk.Tk()
aken.title('Klahvistik')

akna_laius = 800
akna_kõrgus = 400

ekraani_laius = aken.winfo_screenwidth()
ekraani_kõrgus = aken.winfo_screenheight()

keskelx = int(ekraani_laius / 2 - akna_laius / 2 )
keskely = int(ekraani_kõrgus / 2 - akna_kõrgus / 2)

aken.geometry(f'{akna_laius}x{akna_kõrgus}+{keskelx}+{keskely}')

aken.mainloop()

