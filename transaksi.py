import os
import sys
import pandas
import locale
import subprocess
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from pathlib import Path
from tkinter import *
from tkinter import ttk, messagebox

csv = 'keuangan.csv'
dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(dir, csv)

def relative_to_assets(file_path):
    return os.path.join(dir, "assets\\frame0", file_path)

def switch(jenis):
    global button_image_2, button_image_3, button_image_1

    if jenis == 'Pemasukan':
        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Label(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
        )
        button_2.place(
            x=18.0,
            y=59.0,
            width=158.0,
            height=40.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: switch('Pengeluaran'),
            relief="flat"
        )
        button_3.place(
            x=184.0,
            y=59.0,
            width=159.0,
            height=41.0
        )

        combobox['values']=("Uang Masuk", "Gaji", "Investasi")
        combobox.current(0)

    elif jenis == 'Pengeluaran':
        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2_1.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: switch('Pemasukan'),
            relief="flat",
        )
        button_2.place(
            x=18.0,
            y=59.0,
            width=158.0,
            height=40.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3_1.png"))
        button_3 = Label(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        button_3.place(
            x=184.0,
            y=59.0,
            width=159.0,
            height=41.0
        )
        combobox['values']=(
            'Makanan',
            'Transportasi',
            'Kebutuhan Bulanan',
            'Belanja',
            'Pendidikan',
            'Kesehatan',
            'Entertainment'
        )
        combobox.current(0)
    else:
        pass
    
    button_1['command'] = lambda: transaksi(jenis)


def run_file(nama_file):
    dir = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(dir, nama_file)
    window.destroy()
    subprocess.run(["python", file])
    sys.exit()

def transaksi(jenis):
    try:
        jumlah = int(entry_1.get())
        keterangan = entry_2.get()
        kategori = combobox.get()
        tanggal = cal.get()

        if jumlah <= 0:
            raise AssertionError
        else:
            new_data = {
                'Uang': [jumlah if jenis == 'Pemasukan' else jumlah * -1],
                'Kategori': [kategori],
                'Tanggal': [tanggal],
                'Jenis': [jenis],
                'Keterangan': [keterangan],
            }
            new_df = pandas.DataFrame(new_data)
            new_df.to_csv(csv_path, mode='a', index=False, header=False)
            messagebox.showinfo("Sukses", "Transaksi berhasil ditambahkan")
    except AssertionError:
        messagebox.showerror("Error", "Jumlah tidak boleh 0 atau kurang")
    except ValueError:
        messagebox.showerror("Error", "Jumlah yang dimasukkan harus berupa angka")

window = Tk()
window.title('CUSKU')
window.iconbitmap(relative_to_assets('logo.ico'))

window.geometry("360x509")
window.configure(bg = "#1587CC")


canvas = Canvas(
    window,
    bg = "#1587CC",
    height = 509,
    width = 360,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    180.0,
    255.17816162109375,
    image=image_image_1
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Label(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
)
button_2.place(
    x=18.0,
    y=59.0,
    width=158.0,
    height=40.0
)


image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    173.1092529296875,
    160.885986328125,
    image=image_image_2
)

canvas.create_text(
    80.7083740234375,
    143.0166015625,
    anchor="nw",
    text="Jumlah",
    fill="#333333",
    font=("Quicksand Regular", 11 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    52.0,
    175.82183837890625,
    image=image_image_3
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    180.85498046875,
    167.38717651367188,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=104.75048828125,
    y=157.7672119140625,
    width=152.208984375,
    height=17.23992919921875
)

canvas.create_text(
    83.372802734375,
    159.04986572265625,
    anchor="nw",
    text="RP ",
    fill="#333333",
    font=("Quicksand Bold", 13 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: switch('Pengeluaran'),
    relief="flat"
)
button_3.place(
    x=184.0,
    y=59.0,
    width=159.0,
    height=41.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("new_button_4.png"))
button_4 = Label(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_4.place(
    x=14.0,
    y=256.0,
    width=318.3134765625,
    height=50.5938720703125
)

combobox = ttk.Combobox(
    values=("Uang Masuk", "Gaji", "Investasi"),
    state="readonly",
)
combobox.place(
    x=80.0,
    y=280.0,
    width=245
)
combobox.current(0)

button_image_5 = PhotoImage(
    file=relative_to_assets("new_button_5.png"))
button_5 = Label(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_5.place(
    x=14.0,
    y=198.0,
    width=318.3134765625,
    height=49.5938720703125
)

cal = DateEntry(
    window,
    locale='id_ID',
    date_pattern='dd/MM/yyyy',
    selectmode="day",
    state='readonly'
)
cal.place(
    x=80.0,
    y=220.0,
    width=245
)

canvas.create_text(
    87.0,
    24.82183837890625,
    anchor="nw",
    text="Tambahkan Transaksi",
    fill="#FFFFFF",
    font=("Quicksand Bold", 17 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    174.0,
    342.77197265625,
    image=image_image_4
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    171.3775634765625,
    349.2732238769531,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=81.6982421875,
    y=339.65325927734375,
    width=179.358642578125,
    height=17.23992919921875
)

canvas.create_text(
    81.6982421875,
    324.90264892578125,
    anchor="nw",
    text="Keterangan",
    fill="#333333",
    font=("Quicksand Regular", 11 * -1)
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    53.8907470703125,
    340.0,
    image=image_image_5
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: run_file("homepage.py"),
    relief="flat"
)
button_6.place(
    x=18.0,
    y=28.0,
    width=20.0,
    height=20.0
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    52.0,
    158.0,
    image=image_image_6
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: transaksi('Pemasukan'),
    relief="flat"
)
button_1.place(
    x=14.1092529296875,
    y=437.38714599609375,
    width=318.3135986328125,
    height=34.41802978515625
)

try:
    df = pandas.read_csv(csv_path, parse_dates=['Tanggal'], dayfirst=True)
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

df = pandas.read_csv(csv_path)

window.resizable(False, False)
window.mainloop()
