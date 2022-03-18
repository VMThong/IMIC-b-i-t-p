from tkinter import *
from db_conn import *


def them_info_KH():
    insert_customer(entry_ma_khach_hang.get(), entry_ten_khach_hang.get(), entry_diem_tich_luy.get(), entry_dia_chi.get())


customer_GUI_form = Tk()
customer_GUI_form.geometry("420x120")
customer_GUI_form.title("Thêm Customer")

lbl_ma_khach_hang = Label(customer_GUI_form, text="Mã khách hàng: ")
lbl_ten_khach_hang = Label(customer_GUI_form, text="Tên khách hàng: ")
lbl_diem_tich_luy = Label(customer_GUI_form, text="Điểm tích lũy: ")
lbl_dia_chi = Label(customer_GUI_form, text="Địa chỉ: ")

entry_ma_khach_hang = Entry(customer_GUI_form, width=50)
entry_ten_khach_hang = Entry(customer_GUI_form, width=50)
entry_diem_tich_luy = Entry(customer_GUI_form, width=50)
entry_dia_chi = Entry(customer_GUI_form, width=50)

button_add = Button(customer_GUI_form, text="Thêm thông tin", command=them_info_KH)

lbl_ma_khach_hang.grid(row=0, column=0)
entry_ma_khach_hang.grid(row=0, column=1)
lbl_ten_khach_hang.grid(row=1, column=0)
entry_ten_khach_hang.grid(row=1, column=1)
lbl_diem_tich_luy.grid(row=2, column=0)
entry_diem_tich_luy.grid(row=2, column=1)
lbl_dia_chi.grid(row=3, column=0)
entry_dia_chi.grid(row=3, column=1)
button_add.grid(row=4, column=1)

mainloop()
