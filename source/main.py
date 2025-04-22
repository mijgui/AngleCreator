from customtkinter import *  # type: ignore
import math

def clkd():
    draw_angle(int(slA.get()))

def update_label(value):
    value = int(float(value))
    mbA.configure(text=str(value))
    slA.set(value)

def on_label_click(event):
    mbA.place_forget()
    entry_var.set(mbA.cget('text'))
    entry.place(relx=0.5, rely=0.5, anchor='center')
    entry.focus()

def apply_entry_value(event=None):
    try:
        value = int(entry_var.get())
        value = max(0, min(180, value))
        update_label(value)
    except ValueError:
        pass
    entry.place_forget()
    mbA.place(relx=0.5, rely=0.5, anchor='center')

def draw_angle(degrees):
    canvas.delete('all')
    center_x = 150
    center_y = 200
    length = 130
    width = 5

    x1 = center_x + length
    y1 = center_y
    canvas.create_line(center_x, center_y, x1, y1, width=width, fill='black',
                       capstyle='round', joinstyle='round')

    radians = math.radians(degrees)
    x2 = center_x + length * math.cos(radians)
    y2 = center_y - length * math.sin(radians)
    canvas.create_line(center_x, center_y, x2, y2, width=width, fill='black',
                       capstyle='round', joinstyle='round')

    mid_angle = radians / 2
    text_radius = 60
    tx = center_x + text_radius * math.cos(mid_angle)
    ty = center_y - text_radius * math.sin(mid_angle)
    canvas.create_text(tx, ty, text=f'{degrees}°', font=('Arial', 14), fill='black')

app = CTk()
app.geometry('430x470')
app.title('Отрисовщик углов')

btC = CTkButton(app, width=80, height=40, text='Create', command=clkd)
btC.grid(row=1, column=6, padx=20, pady=0, sticky='ew')

slA = CTkSlider(app, from_=0, to=180, command=update_label)
slA.grid(row=1, column=0, padx=20, pady=30, sticky='ew')

fA = CTkFrame(app, width=70, height=50)
fA.grid_propagate(False)
fA.grid(row=1, column=4, padx=0, pady=30)

mbA = CTkLabel(fA, text='0', font=('Arial', 20))
mbA.place(relx=0.5, rely=0.5, anchor='center')
mbA.bind('<Button-1>', on_label_click)

entry_var = StringVar()
entry = CTkEntry(fA, textvariable=entry_var, font=('Arial', 20), width=60)
entry.bind('<Return>', apply_entry_value)
entry.bind('<FocusOut>', apply_entry_value)

canvas = CTkCanvas(app, width=300, height=300, bg='white', highlightthickness=0)
canvas.grid(row=2, column=0, columnspan=7, pady=20)

update_label(0)

app.mainloop()
