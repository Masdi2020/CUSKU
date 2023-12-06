import os
import sys
import subprocess
import pandas
import locale
from datetime import datetime
from pathlib import Path
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, messagebox

locale.setlocale(locale.LC_TIME, 'id_ID')
locale.setlocale(locale.LC_NUMERIC, 'id_ID')

csv = 'keuangan.csv'
dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(dir, csv)

def hari(tanggal):
    return tanggal.strftime("%A, %d %b %Y")

def relative_to_assets(file_path):
    return os.path.join(dir, "assets\\frame5", file_path)

def run_file(nama_file):
    file = os.path.join(dir, nama_file)
    window.destroy()
    subprocess.run(["python", file])
    sys.exit()

def calculate_pos(length, char):
    dot = char.count(".")
    rp = 320 - 7.75*length - 3.5*dot
    return rp

max_length = 0
max_char = ''

window = Tk()
window.title('CUSKU')
window.iconbitmap(relative_to_assets('logo.ico'))

window.geometry("360x509")
window.configure(bg = "#4381DE")

canvas = Canvas(
    window,
    bg = "#4381DE",
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
    255.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    102.0,
    229.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    255.703125,
    229.973876953125,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    214.8974609375,
    228.9515380859375,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    214.8935546875,
    229.12841796875,
    image=image_image_5
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: run_file("transaksi.py"),
    relief="flat"
)
button_2.place(
    x=208.0,
    y=107.0,
    width=127.0,
    height=36.0
)

canvas.create_text(
    238.254638671875,
    213.82373046875,
    anchor="nw",
    text="Pengeluaran",
    fill="#FFFFFF",
    font=("Lato Bold", 10 * -1)
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    102.06640625,
    228.973876953125,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    55.548583984375,
    228.6697998046875,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    55.48486328125,
    229.045166015625,
    image=image_image_8
)

canvas.create_text(
    79.097412109375,
    213.6697998046875,
    anchor="nw",
    text="Pemasukan",
    fill="#FFFFFF",
    font=("Lato Bold", 10 * -1)
)

canvas.create_text(
    29.07373046875,
    261.9833984375,
    anchor="nw",
    text=" Riwayat Transaksi",
    fill="#333333",
    font=("Quicksand Bold", 14 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: run_file("riwayat.py"),
    relief="flat"
)
button_1.place(
    x=305.0,
    y=260.0,
    width=22.0,
    height=26.24853515625
)

# bg
image_image_21 = PhotoImage(
    file=relative_to_assets("image_21.png"))
image_21 = canvas.create_image(
    178.0,
    85.0,
    image=image_image_21
)

image_image_22 = PhotoImage(
    file=relative_to_assets("image_22.png"))
image_22 = canvas.create_image(
    178.812255859375,
    84.53680419921875,
    image=image_image_22
)

image_image_23 = PhotoImage(
    file=relative_to_assets("image_23.png"))
image_23 = canvas.create_image(
    273.845703125,
    88.34918212890625,
    image=image_image_23
)

image_image_24 = PhotoImage(
    file=relative_to_assets("image_24.png"))
image_24 = canvas.create_image(
    44.0,
    34.0,
    image=image_image_24
)

canvas.create_text(
    60.0,
    27.0,
    anchor="nw",
    text="CUSKU",
    fill="#FFFFFF",
    font=("MontserratRoman ExtraBold", 12 * -1)
)

canvas.create_text(
    32.06640625,
    179.03802490234375,
    anchor="nw",
    text="Catatan Keuangan",
    fill="#333333",
    font=("Quicksand Bold", 14 * -1)
)

canvas.create_text(
    31.0,
    58.0,
    anchor="nw",
    text="Saldo Anda",
    fill="#FFFFFF",
    font=("Quicksand Bold", 16 * -1)
)

try:
    df = pandas.read_csv(csv_path, parse_dates=['Tanggal'], dayfirst=True)
except FileNotFoundError:
    jawaban = messagebox.askyesno(
        "File Tidak Ditemukan!",
        "File tidak ditemukan. Ingin membuat file?",
        icon='error',
        default=messagebox.YES,
        detail='Pilih "Yes" untuk membuat file, "No" untuk membatalkan.'
    )
    if jawaban:
        header = ["Uang", "Kategori", "Tanggal", "Jenis", "Keterangan"]
        df = pandas.DataFrame(columns=header)
        df.to_csv(csv_path, index=False)
    else:
        sys.exit()

if 1 <= len(df) < 4:
    batas = (len(df) + 1) * -1
elif len(df) >= 4:
    batas = -5
else:
    batas = False

if batas:
    for i in range(-1, batas, -1):
        value = str(abs(df.iloc[i, 0]))
        if len(value) > max_length:
            max_length = len(value)
            max_char = locale.format_string("%.0f", int(value), grouping=True)
        else:
            pass
else:
    pass

posisi_rp = calculate_pos(max_length, max_char)

canvas.create_text(
    238.254638671875,
    230.39569091796875,
    anchor="nw",
    text="-Rp." + locale.format_string('%.0f', abs(df[df['Jenis'] == 'Pengeluaran']['Uang'].sum()), grouping=True),
    fill="#E85454",
    font=("Quicksand Bold", 11 * -1)
)

canvas.create_text(
    79.097412109375,
    229.9168701171875,
    anchor="nw",
    text="Rp." + locale.format_string('%.0f', abs(df[df['Jenis'] == 'Pemasukan']['Uang'].sum()), grouping=True),
    fill="#3AD58B",
    font=("Quicksand Bold", 11 * -1)
)

if len(df) >= 1:
    image_image_9 = PhotoImage(
        file=relative_to_assets("image_9.png"))
    image_9 = canvas.create_image(
        179.0,
        313.0,
        image=image_image_9
    )
    
    image_image_10 = PhotoImage(
        file=relative_to_assets("image_10.png"))
    image_10 = canvas.create_image(
        179.0,
        313.0,
        image=image_image_10
    )
    
    canvas.create_text(
        46.0,
        292.0,
        anchor="nw",
        text=hari(df.iloc[-1, 2]),
        fill="#3570CA",
        font=("Quicksand Bold", 11 * -1)
    )
    
    if pandas.isna(df.iloc[-1, 4]):
        pass
    else:
        canvas.create_text(
            87.0,
            321.0,
            anchor="nw",
            text=df.iloc[-1, 4],
            fill="#737373",
            font=("Lato Regular", 10 * -1)
        )
    
    canvas.create_text(
        87.0,
        308.0,
        anchor="nw",
        text=df.iloc[-1, 1],
        fill="#333333",
        font=("Quicksand Bold", 12 * -1)
    )
    
    canvas.create_text(
        320.0,
        307.0,
        anchor="ne",
        text=locale.format_string('%.0f', abs(df.iloc[-1, 0]), grouping=True),
        fill="#333333",
        font=("Lato Bold", 13 * -1)
    )
    
    canvas.create_text(
        posisi_rp,
        307.0,
        anchor="ne",
        text="+Rp" if df.iloc[-1, 0] >= 0 else "-Rp",
        fill="#333333",
        font=("Lato Bold", 13 * -1)
    )
    
    image_image_11 = PhotoImage(
        file=relative_to_assets(df.iloc[-1, 1]+".png")
    )
    image_11 = canvas.create_image(
        60.0,
        320.0,
        image=image_image_11
    )
else:
    pass

if len(df) >= 2:
    image_image_15 = PhotoImage(
        file=relative_to_assets("image_15.png"))
    image_15 = canvas.create_image(
        179.0,
        370.0,
        image=image_image_15
    )

    image_image_16 = PhotoImage(
        file=relative_to_assets("image_16.png"))
    image_16 = canvas.create_image(
        179.0,
        369.710205078125,
        image=image_image_16
    )

    canvas.create_text(
        48.0,
        349.0,
        anchor="nw",
        text=hari(df.iloc[-2, 2]),
        fill="#3570CA",
        font=("Quicksand Bold", 11 * -1)
    )

    if pandas.isna(df.iloc[-2, 4]):
        pass
    else:
        canvas.create_text(
            87.0,
            378.0,
            anchor="nw",
            text=df.iloc[-2, 4],
            fill="#737373",
            font=("Lato Regular", 10 * -1)
        )

    canvas.create_text(
        89.0,
        365.0,
        anchor="nw",
        text=df.iloc[-2, 1],
        fill="#333333",
        font=("Quicksand Bold", 12 * -1)
    )

    canvas.create_text(
        320.0,
        364.0,
        anchor="ne",
        text=locale.format_string('%.0f', abs(df.iloc[-2, 0]), grouping=True),
        fill="#333333",
        font=("Lato Bold", 13 * -1)
    )

    canvas.create_text(
        posisi_rp,
        364.0,
        anchor="ne",
        text="+Rp" if df.iloc[-2, 0] >= 0 else "-Rp",
        fill="#333333",
        font=("Lato Bold", 13 * -1)
    )

    image_image_17 = PhotoImage(
        file=relative_to_assets(df.iloc[-2, 1]+".png"))
    image_17 = canvas.create_image(
        61.0,
        377.0,
        image=image_image_17
    )
else:
    pass

if len(df) >= 3:
    image_image_12 = PhotoImage(
        file=relative_to_assets("image_12.png"))
    image_12 = canvas.create_image(
        179.0,
        426.0,
        image=image_image_12
    )

    image_image_13 = PhotoImage(
        file=relative_to_assets("image_13.png"))
    image_13 = canvas.create_image(
        179.0,
        426.0,
        image=image_image_13
    )

    canvas.create_text(
        48.0,
        406.0,
        anchor="nw",
        text=hari(df.iloc[-3, 2]),
        fill="#3570CA",
        font=("Quicksand Bold", 11 * -1)
    )

    if pandas.isna(df.iloc[-3, 4]):
        pass
    else:
        canvas.create_text(
            87.0,
            435.0,
            anchor="nw",
            text=df.iloc[-3, 4],
            fill="#737373",
            font=("Lato Regular", 10 * -1)
        )

    canvas.create_text(
        89.0,
        422.0,
        anchor="nw",
        text=df.iloc[-3, 1],
        fill="#333333",
        font=("Quicksand Bold", 12 * -1)
    )

    canvas.create_text(
        320.0,
        421.0,
        anchor="ne",
        text=locale.format_string('%.0f', abs(df.iloc[-3, 0]), grouping=True),
        fill="#333333",
        font=("Lato Bold", 13 * -1)
    )

    canvas.create_text(
        posisi_rp,
        421.0,
        anchor="ne",
        text="+Rp" if df.iloc[-3, 0] >= 0 else "-Rp",
        fill="#333333",
        font=("Lato Bold", 13 * -1)
    )

    image_image_14 = PhotoImage(
        file=relative_to_assets(df.iloc[-3, 1]+".png"))
    image_14 = canvas.create_image(
        61.0,
        433.0,
        image=image_image_14
    )
else:
    pass

if len(df) >= 4:
    image_image_18 = PhotoImage(
        file=relative_to_assets("image_18.png"))
    image_18 = canvas.create_image(
        179.0,
        482.0,
        image=image_image_18
    )
    
    image_image_19 = PhotoImage(
        file=relative_to_assets("image_19.png"))
    image_19 = canvas.create_image(
        179.0,
        482.06884765625,
        image=image_image_19
    )
    
    canvas.create_text(
        48.0,
        463.0,
        anchor="nw",
        text=hari(df.iloc[-4, 2]),
        fill="#3570CA",
        font=("Quicksand Bold", 11 * -1)
    )
    
    if pandas.isna(df.iloc[-4, 4]):
        pass
    else:
        canvas.create_text(
            87.0,
            492.0,
            anchor="nw",
            text=df.iloc[-4, 4],
            fill="#737373",
            font=("Lato Regular", 10 * -1)
        )
    
    canvas.create_text(
        89.0,
        479.0,
        anchor="nw",
        text=df.iloc[-4, 1],
        fill="#333333",
        font=("Quicksand Bold", 12 * -1)
    )
    
    canvas.create_text(
        320.0,
        478.0,
        anchor="ne",
        text=locale.format_string('%.0f', abs(df.iloc[-4, 0]), grouping=True),
        fill="#333333",
        font=("Lato Bold", 13 * -1)
    )
    
    canvas.create_text(
        posisi_rp,
        478.0,
        anchor="ne",
        text="+Rp" if df.iloc[-4, 0] >= 0 else "-Rp",
        fill="#333333",
        font=("Lato Bold", 13 * -1)
    )
    
    image_image_20 = PhotoImage(
        file=relative_to_assets(df.iloc[-4, 1]+".png"))
    image_20 = canvas.create_image(
        61.0,
        490.0,
        image=image_image_20
    )
else:
    pass

canvas.create_text(
    30.0,
    85.0,
    anchor="nw",
    text=("Rp" if df['Uang'].sum() >= 0 else "-Rp") + locale.format_string('%.0f', abs(df['Uang'].sum()), grouping=True),
    fill="#FFFFFF",
    font=("Quicksand Bold", 22 * -1)
)

window.resizable(False, False)
window.mainloop()
