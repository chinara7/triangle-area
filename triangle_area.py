import math
import tkinter as tk
import tkinter.font as font


def calculate_area():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a + b > c and a + c > b and b + c > a and abs(a - b) < c and abs(a - c) < b and abs(b - c) < a:
            s = (a + b + c) / 2
            triangle_area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            result_label.config(text="NƏTİCƏ: {}".format(triangle_area), font=("Arial", 40, "bold"), fg="#4C7B6D")
        else:
            result_label.config(text="XƏTA: Daxil edilən dəyərlər üçbucaq yaratmır", font=("Arial", 30),
                                fg="red")
    except ValueError:
        result_label.config(text="XƏTA: Tərəflərə yalnız ədəd daxil edə bilərsiniz.", font=("Arial", 30), fg="red")


root = tk.Tk()
root.geometry("1150x700")
root.configure(bg="#101726")
root.title("Üçbucağın sahəsi")

font_size = font.Font(size=16)

title_label = tk.Label(
    root,
    text='ÜÇBUCAĞIN HƏR 3 TƏRƏFİNİ UYĞUN XANALARDA QEYD EDİB \n"SAHƏNİ HESABLA" DÜYMƏSİNƏ KLİKLƏYİN ',
    font=("Arial", 22, "bold"),
    bg="#101726",
    fg="white"
)
title_label.pack(pady=40)

frame = tk.Frame(root, bg="#101726")
frame.pack(pady=20)

label_a = tk.Label(frame, text="Tərəf 1", font=font_size, bg="#101726", fg="white")
label_a.pack(side="left", padx=20)

entry_a = tk.Entry(frame, font=font_size, border=0)
entry_a.pack(side="left", padx=5)

label_b = tk.Label(frame, text="Tərəf 2", font=font_size, bg="#101726", fg="white")
label_b.pack(side="left", padx=20)

entry_b = tk.Entry(frame, font=font_size, border=0)
entry_b.pack(side="left", padx=5)

label_c = tk.Label(frame, text="Tərəf 3", font=font_size, bg="#101726", fg="white")
label_c.pack(side="left", padx=20)

entry_c = tk.Entry(frame, font=font_size, border=0)
entry_c.pack(side="left", padx=5)

calculate_button = tk.Button(
    root,
    text="Sahəni hesabla",
    font=("Arial", 20),
    command=calculate_area,
    border=0,
    relief="solid",
    bg="#7393C2",
    fg="white",
    activebackground="#6EA993",
    activeforeground="white",
)
calculate_button.pack(pady=100)

result_label = tk.Label(root, text="", font=("Arial", 30), anchor="sw", bg="#101726")
result_label.pack(side="bottom", padx=20, pady=40, anchor="sw")

root.mainloop()
