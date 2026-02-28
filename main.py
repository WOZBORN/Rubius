import tkinter

import db
import tkinter as tk
from tkinter import ttk

db.init_db()

def button_clicked():
    print("Кнопка нажата!")

root = tk.Tk() # Главное окно
# Фрейм, в котором мы будем создавать все элементы UI (User Interface)
frame = ttk.Frame(root)
frame.grid()
# Текстовое поле
ttk.Label(frame, text="Дневник лудомана").grid(column=0, row=0)
# Кнопка
ttk.Button(frame, text="Кнопка", command=button_clicked).grid(column=0, row=1)

# db.add_debt("МКК ЗаймВсемБезПроцентовКоллекторовНеБудетКлянемся", "22.02.2026", 1000000)
"ЭТО МОЖНО ИСПОЛЬЗОВАТЬ КАК ФУНКЦИЮ ДЛЯ КНОПКИ"
db.delete_debt(3)


for debt in db.get_debts():
    print(debt)

root.mainloop()