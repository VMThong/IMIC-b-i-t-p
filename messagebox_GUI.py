import tkinter as tk
from functools import partial
from future.moves.tkinter import messagebox
from tkinter.ttk import Combobox
def my_function():
    messagebox.showerror(title="Thông báo", message= cbx_option.get())

my_form = tk.Tk() # Code này dùng tạo form
lbl_name= tk.Label(master= my_form,text= "Nhãn của bảng") #Tạo Lable
lbl_name.grid(row=0, column=0)

entr_number_1=tk.Entry(master=my_form,width=50) #Tạo Entry
entr_number_1.grid(row=0, column=1)

button_name=tk.Button(master=my_form, text="button name", command=(my_function)) #Tạo Button
button_name.grid(row=1, column=0)

cbx_option= Combobox(value=('Giá trị 1', 'Giá trị 2', 'Giá trị 3'),width=50)
cbx_option.grid(row=1, column=1)

my_form.mainloop() # Đây là code để hiển thị/display form


