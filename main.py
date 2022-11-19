import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Ncrypt')
root.resizable(False,False)


#font
current_font = ("Arial Bold", 15)

# declare
key_loc = tk.Variable()
file_loc = tk.Variable()

file_dir = Entry(root,width=70,textvariable=file_loc)
key_dir = Entry(root,width=70,textvariable=key_loc)

browse_file_button = Button(root,font=current_font, text='Browse directory',)
browse_key_button = Button(root,font=current_font, text='Browse key',)

main_label = Label(root,font=current_font, text='******************* Welcome To Ncrypt *******************\n\n- Browse for your key\n\n- Browse for the directory\n\n- Then encrypt / decrypt\n')

encrypt_button = Button(root,font=current_font, text='Encrypt Directory',height=2, width=4,)
decrypt_button = Button(root,font=current_font, text='Decrypt Directory',height=2, width=4,)

# grid
file_dir.grid(column=0, row=0, columnspan=2, sticky=(W), padx=10,pady=10)
key_dir.grid(column=0,row=1, columnspan=2, sticky=(W),padx=10,pady=10)

browse_file_button.grid(column=3, row=0, sticky=(E), padx=10,pady=10)
browse_key_button.grid(column=3, row=1, sticky=(E), padx=10,pady=10)

main_label.grid(column=0, row=2, columnspan=4, padx=10,pady=10)

encrypt_button.grid(column=0,columnspan=1 , row=3, sticky=(S,E,W), padx=10,pady=10)
decrypt_button.grid(column=1,columnspan=4 , row=3, sticky=(S,E,W), padx=10,pady=10)

# weights
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=3)

root,mainloop()