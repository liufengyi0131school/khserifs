import pathlib
import winsound
import random
import tkinter as tk
from tkinter import messagebox
while True: 
    path = pathlib.Path()
    for i in path.iterdir():
        dir_path = pathlib.Path(i)
        if dir_path.is_dir():
            a1 = list(list(dir_path.iterdir()))
            random.shuffle(a1)
            for j in list(a1):
                j_pathlib = pathlib.Path(j)
                if j_pathlib.is_file() and j_pathlib.suffix.lower() == ".wav":
                    winsound.PlaySound(str(j_pathlib),winsound.SND_FILENAME)
                    with open(str(j_pathlib).replace(".wav",".txt"),"r",encoding="utf-8") as file:
                        root = tk.Tk()
                        textfeld = tk.Entry(root,width=50)
                        textfeld.pack()
                        def check():
                            global root,textfeld,checkbutton,check
                            if str(textfeld.get().strip().lower()) == str(str(file.read()).strip().lower()):
                                
                                messagebox.showinfo("richtig","richtig")
                            else:
                                messagebox.showerror("falsche","falsche")
                            root.destroy()
                            del root,textfeld,checkbutton,check
                        checkbutton = tk.Button(root,text="check",command=check)
                        checkbutton.pack()
                        root.mainloop()



                    
