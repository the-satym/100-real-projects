#date: 15 jan 2025
import qrcode
from tkinter import *
import os
from pathlib import Path

root = Tk()
root.geometry("300x300")
root.title("QR Code generator")
label1=Label(root,text="enter your URL here").grid(row=0,column=1)
label2=Label(root,text="enter file name you want to save as").grid(row=3,column=1)

def entry_widget1():
    placeholder1="enter your URL here"
    e=Entry(root, fg='grey')
    e.grid(row=1,column=1)
    e.insert(0, placeholder1)
    e.bind("<FocusIn>", lambda event: e.delete(0, END) if e.get() == placeholder1 else None)
    e.bind("<FocusOut>", lambda event: e.insert(0, placeholder1) if not e.get() else None)

def entry_widget2():
    placeholder2 = "enter file name you want to save as"
    f=Entry(root, fg='grey')
    f.grid(row=4,column=1)
    f.insert(0, placeholder2)
    f.bind("<FocusIn>", lambda event: f.delete(0, END) if f.get() == placeholder2 else None)
    f.bind("<FocusOut>", lambda event: f.insert(0, placeholder2) if not f.get() else None)


def button_1(a,b):
    data = a.get()
    file = b.get()
    download_folder=str(Path.home()/"downloads")
    file_path=os.path.join(download_folder,file)
    qr = qrcode.QRCode(box_size=20, border=5)
    qr.add_data(data)
    image = qr.make_image(fill_color="black", back_color="white")
    image.save(file_path)
    print(f'QR Code is saved at {file_path}')

button1=Button(root,text="generate qr code",padx=15,pady=8,command=button_1)
button1.grid(row=6,column=1)

a=entry_widget1()
b=entry_widget2()

root.mainloop()