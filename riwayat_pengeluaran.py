
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

import os
import sys
import pandas
import locale
import subprocess
from tkinter import *
from datetime import datetime
from PIL import Image, ImageTk

from pathlib import Path

# Explicit imports to satisfy Flake8
from tkinter import ttk, messagebox


csv = 'keuangan.csv'
image_dict = {}
image_list = []

locale.setlocale(locale.LC_NUMERIC, 'id_ID')
locale.setlocale(locale.LC_TIME, 'id_ID')

def relative_to_assets(file_path):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, "assets\\frame6", file_path)

def run_file(nama_file):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(current_dir, nama_file)
    window.destroy()
    subprocess.run(["python", file])
    sys.exit()

def scroll_config(event):
    canvas_b.configure(scrollregion=canvas_b.bbox('all'))
    canvas_b.yview_moveto(0)

    if canvas_b.winfo_width() >= canvas_b.winfo_reqwidth():
        canvas_b.unbind('<Left>')
        canvas_b.unbind('<Right>')
    else:
        canvas_b.bind('<Left>', lambda e: canvas_b.xview_scroll(-1, 'units'))
        canvas_b.bind('<Right>', lambda e: canvas_b.xview_scroll(1, 'units'))

    if canvas_b.winfo_height() >= canvas_b.winfo_reqheight():
        canvas_b.unbind('<Up>')
        canvas_b.unbind('<Down>')
    else:
        canvas_b.bind('<Up>', lambda e: canvas_b.yview_scroll(-1, 'units'))
        canvas_b.bind('<Down>', lambda e: canvas_b.yview_scroll(1, 'units'))
        
    if canvas_b.winfo_height() >= canvas_b.winfo_reqheight():
        canvas_b.unbind('<MouseWheel>')
        scrollbar.pack_forget()
    else:
        canvas_b.bind_all('<MouseWheel>', lambda f: canvas_b.yview_scroll(int(-1 * (f.delta / 120)), 'units'))
        scrollbar.pack(side='right', fill='y')
        scrollbar.place(
            x=345,
            height = 389
        )

def hari(tanggal):
    return tanggal.strftime("%A, %d %b %Y")

def del_child():
    for child in frame_b.winfo_children():
        child.destroy()

def callback(menu):
    sorted_df = pengeluaran.sort_values(by='Tanggal', ascending=False)
    del_child()
    transaksi(sorted_df)
    
def callback1(menu):
    sorted_df = pengeluaran.sort_values(by='Tanggal')
    del_child()
    transaksi(sorted_df)

def callback2(menu):
    sorted_df = pengeluaran.sort_values(by='Uang', ascending=False)
    del_child()
    transaksi(sorted_df)

def callback3(menu):
    sorted_df = pengeluaran.sort_values(by='Uang')
    del_child()
    transaksi(sorted_df)

def transaksi(data):
    if len(data):
        for j in range(len(data)):
            value = data.iloc[j, 0]
            kategori = data.iloc[j, 1]
            tanggal = data.iloc[j, 2]
            keterangan = data.iloc[j, 4]

            teks_rp = "-Rp"

            uang = locale.format_string("%.0f", abs(value), grouping=True)

            frame1 = Frame(
                frame_b,
                width=image.width,
                height=image.height,
                relief=FLAT,
                borderwidth=0,
                highlightthickness=0,
                pady=5
            )
            frame1.place(anchor=CENTER, relx=0.5, rely=0)

            background_label = Label(frame1, image=photo)
            background_label.image = photo
            background_label.place(relheight=1, relwidth=1)

            uang_label = Label(
                frame1,
                text=uang,
                fg='#333333',
                bg='white',
                highlightthickness=0,
                border=0,
                font=("Lato Bold", 13 * -1)
            )
            uang_label.place(relx=0.975, rely=0.5, anchor=E)

            rp_label = Label(
                frame1,
                text = teks_rp,
                fg = '#333333',
                bg = 'white',
                highlightthickness = 0,
                border=0,
                font=("Lato Bold", 13 * -1)
            )
            rp_label.place(relx=posisi_rp, rely=0.5, anchor=CENTER)

            img_path=relative_to_assets(kategori + ".png")
            img = Image.open(img_path)
            photo1 = ImageTk.PhotoImage(img)
            image_dict[kategori] = photo1

            icon_label = Label(
                frame1,
                image=image_dict[kategori],
                bg='white'
            )
            icon_label.image = photo1
            icon_label.place(relx=0.025, rely=0.60, anchor=W)

            tanggal_label = Label(
                frame1,
                text=hari(tanggal),
                fg='#3570CA',
                bg='white',
                highlightthickness=0,
                border=0,
                font=("Quicksand Bold", 11 * -1)
            )
            tanggal_label.place(relx=0.040, rely=0.20, anchor=W)

            kategori_label = Label(
                frame1,
                text=kategori,
                fg='#333333',
                bg='white',
                highlightthickness=0,
                border=0,
                font=("Quicksand Bold", 12 * -1)
            )
            kategori_label.place(relx=0.15, rely=0.5, anchor=W)

            if pandas.isna(df.iloc[j, 4]):
                pass
            else:
                keterangan_label = Label(
                    frame1,
                    text=keterangan,
                    fg='#737373',
                    bg='white',
                    highlightthickness=0,
                    border=0,
                    font=("Lato Regular", 10 * -1)
                )
                keterangan_label.place(relx=0.15, rely=0.75, anchor=W)

            frame1.grid(row=j)
    else:
        pass

def calculate_pos(length, char):
    count_dot = char.count(".")
    rp = 87 - 1.75*(length-1) - 2*count_dot
    posisi_rp = rp / 100
    return posisi_rp

window = Tk()
window.title('CUSKU')
window.iconbitmap(relative_to_assets('logo.ico'))

window.geometry("360x509")
window.configure(bg = "#FFFFFF")

image_path = relative_to_assets('image_2.png')
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

bg = Canvas(
    master = window,
    height = 509,
    width = 360,
    highlightthickness = '0',
    relief = 'ridge'
)
bg.place(x=0, y=0)

image_1 = PhotoImage(
    file=relative_to_assets('image_1.png')
)
image_1_1 = bg.create_image(
    180,
    255,
    image=image_1
)

bg.create_text(
    109.98583984375,
    16.88836669921875,
    anchor="nw",
    text="Riwayat Transaksi",
    fill="#FFFFFF",
    font=("Quicksand Bold", 17 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets('button_1.png'))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: run_file("riwayat_pemasukan.py"),
    relief="flat"
)
button_1.place(
    x=24.0,
    y=46.0,
    width=147.0,
    height=38.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Label(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_2.place(
    x=195.0,
    y=46.0,
    width=141.0,
    height=38.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_3.place(
    x=261.0,
    y=101.0,
    width=80.0,
    height=19.0
)
button_3.bind("<Button-1>", lambda e: menu.post(e.x_root, e.y_root))

# Buat menu popup
menu = Menu(window, tearoff=0)
menu.add_command(label="Transaksi Terbaru", command = lambda: callback(menu))
menu.add_command(label="Transaksi Terlama", command = lambda: callback1(menu))
menu.add_command(label="Transaksi Terbesar", command = lambda: callback2(menu))
menu.add_command(label="Transaksi Terkecil", command = lambda: callback3(menu))

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: run_file("homepage.py"),
    relief="flat"
)
button_4.place(
    x=16.0,
    y=18.0,
    width=20.0,
    height=20.0
)

b=Frame(
    window,
    height = 389,
    width = 360,
    bg="#efefef",
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

b.pack(fill=BOTH, expand=1)
b.place(x=0, y=120)

canvas_b = Canvas(
    b,
    background="#efefef",
    highlightthickness=0,
    height = 389,
    width = 360
)
canvas_b.pack(side=TOP, fill=BOTH, expand=1)

scrollbar = ttk.Scrollbar(
    b,
    orient=VERTICAL,
    command=canvas_b.yview,
)

canvas_b.configure(yscrollcommand=scrollbar.set)
canvas_b.bind('<Configure>', scroll_config)

frame_b = Frame(
    canvas_b,
)
frame_b.pack(side=TOP, fill=BOTH)
scrollbar_width = scrollbar.winfo_reqwidth()
canvas_b.create_window((canvas_b.winfo_reqwidth()/2 - scrollbar_width/2, 0), window=frame_b, anchor='center')

try:
    df = pandas.read_csv(csv, parse_dates=['Tanggal'], dayfirst=True)
except FileNotFoundError:
    jawaban = messagebox.askyesnocancel(
        "File Tidak Ditemukan!",
        "File tidak ditemukan. Ingin menjalankan homepage.py untuk membuat file?",
        icon='error',
        default=messagebox.YES,
        detail='Pilih "Yes" untuk membuat file dari homepage.py, "No" untuk membuat file dari program ini, atau "Cancel" untuk membatalkan.'
    )

    if jawaban is not None:
        if jawaban:
            run_file('homepage.py')
        else:
            header = ["Uang", "Kategori", "Tanggal", "Jenis", "Keterangan"]
            df = pandas.DataFrame(columns=header)
            df.to_csv('keuangan.csv', index=False)
    else:
        sys.exit()

pengeluaran = df[df['Jenis'] == 'Pengeluaran']

max_length = 0
max_char = ''
for i in range(len(pengeluaran)):
    value = pengeluaran.iloc[i, 0]
    uang = str(abs(value))
    if len(uang) > max_length:
        max_length = len(uang)
        max_char = locale.format_string("%.0f", int(uang), grouping=True)

posisi_rp = calculate_pos(max_length, max_char)

transaksi(pengeluaran)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)


window.resizable(False, False)
window.mainloop()
