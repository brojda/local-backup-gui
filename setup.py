import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import *
from PIL import ImageTk, Image
import os, shutil
app = tk.Tk()
app.geometry("700x500")
app.title("Pybackup setup")
app.iconbitmap("./images/logo.ico")
app.resizable(False, False)
def select_folder():
    path_dialog = filedialog.askdirectory(title="Select a folder")
    path_var.set(f"{path_dialog}/pybackup")
def start():
    global btn, label
    btn.destroy()
    shortcut_btn.destroy()
    startup_btn.destroy()
    launch_btn.destroy()
    label = tk.Label(frame, text="Ecxtracting fils ...", font=('calibre',14,'normal'))
    label.grid(row=1, column=1, pady = 10)
    progress = Progressbar(frame, orient = tk.HORIZONTAL, length = 400, mode = 'determinate')
    progress.grid(row=2, column=1)
    launch.get()
    shortcut.get()
    path = path_var.get()
    btn = tk.Button(frame, text="Finish", width = 15, state=tk.DISABLED)
    btn.grid(row=3, column=2, pady = 260)
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)
    files = os.listdir("./files")
    step = 100 / len(files)
    for file in files:
        shutil.copy(f"./files/{file}", path)
        progress['value'] += step
    if startup.get() :
        startup()
def save_path():
    global btn, path_var, path, label, browsingbtn
    div.destroy()
    btn.destroy()
    path_var = tk.StringVar()
    label = tk.Label(frame, text="Select app location", font=('calibre',14,'normal'))
    label.grid(row=1, column=1, pady = 10)
    path_var.set("C:/Program Files/pybackup")
    path = tk.Entry(frame,textvariable = path_var, font=('calibre',10,'normal'), width = 50)
    path.grid(row=2, column=1)
    browsingbtn = tk.Button(frame, text="Browse", width = 15, command= select_folder)
    browsingbtn.grid(row=2, column=2)
    btn = tk.Button(frame, text="Next", width = 15, command = setting)
    btn.grid(row=3, column=2, pady = 210, padx = 47)
def setting():
    global shortcut, launch, startup, shortcut_btn, startup_btn, launch_btn, btn
    label.destroy()
    div.destroy()
    path.destroy()
    browsingbtn.destroy()
    btn.destroy()
    shortcut = tk.IntVar()
    startup = tk.IntVar()
    launch = tk.IntVar()
    shortcut_btn = tk.Checkbutton(frame, text = "Creat a shortcut on Desktop                  ",
    variable = shortcut,
    onvalue = 1,
    offvalue = 0,
    height = 2,
    width = 30)

    startup_btn = tk.Checkbutton(frame, text = "Run the app when computer is startup",
    variable = startup,
    onvalue = 1,
    offvalue = 0,
    height = 2,
    width = 30)

    launch_btn = tk.Checkbutton(frame, text = "Launch the app when setup is done    ",
    variable = launch,
    onvalue = 1,
    offvalue = 0,
    height = 2,
    width = 30)
    startup_btn.select()
    launch_btn.select()
    shortcut_btn.select()
    startup_btn.grid(row=1, column=1)
    shortcut_btn.grid(row=2, column=1)
    launch_btn.grid(row=3, column=1)
    btn = tk.Button(app, text="Next", width = 15, command = start)
    btn.grid(row=2, column=2, pady = 163, padx = 159)

# <body
frame = tk.Frame(app, width=600, height=400)
frame.grid(row=0, column=0)
img = Image.open("./images/logo.png")
img = img.resize((70, 70))
img = ImageTk.PhotoImage(img)
label = tk.Label(frame, image=img)
label.grid(row=0, column=0, pady = 50, padx = 50)
label = tk.Label(frame, text="WELCOME TO PYBACKUP")
label.grid(row=0, column=0)
div = tk.Label(frame, text="Welcom to setup. Make sure that you are running this file as Administrator \n don't close this program while it is running")
div.grid(row=1, column=1, pady = 0, padx = 0)
btn = tk.Button(app, text="Next", width = 15, command = save_path)
btn.grid(row=2, column=2, pady = 250)
app.mainloop()
