import tkinter as tk 
from tkinter import *
import tkinter.messagebox

root = tk.Tk()
 
root.title("Конвертер валют")
 
Tops = Frame(root, bg = '#e6e5e5', pady=2, width=1850, height=100, relief="ridge")
Tops.grid(row=0, column=0)
 
headlabel = tk.Label(Tops, font=('lato black', 19, 'bold'), text='Конвертер валют ',
                    bg='#e6e5e5', fg='black')
headlabel.grid(row=1, column=0, sticky=W)
 
variable1 = tk.StringVar(root)
variable2 = tk.StringVar(root)
 
variable1.set("Валюта")
variable2.set("Валюта")

#Функция для конвертации валюты в режиме реального времени
def RealTimeCurrencyConversion():
    from forex_python.converter import CurrencyRates
    c = CurrencyRates()
    from_currency = variable1.get()
    to_currency = variable2.get()
    if (Amount1_field.get() == ""):
        tkinter.messagebox.showinfo("Ошибка!", "Сумма не введена.\nПожалуйста, укажите нужную сумму.")
    elif (from_currency == "Валюта" or to_currency == "Валюта"):
        tkinter.messagebox.showinfo("Ошибка!",
                                    "Валюта не выбрана.\nПожалуйста, выберите ОТ и ДО Меню формы валюты.")
 
    else:
        new_amt = c.convert(from_currency, to_currency, float(Amount1_field.get()))
        new_amount = float("{:.4f}".format(new_amt))
        Amount2_field.insert(0, str(new_amount))
 
#удаление всех данных, введенных пользователем
def clear_all():
    Amount1_field.delete(0, tk.END)
    Amount2_field.delete(0, tk.END)
#CurrenyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR"]
CurrenyCode_list = ['USD', 'IDR','BGN','ILS','GBP','DKK','CAD','JPY','HUF','RON','MYR','SEK','SGD','HKD','AUD','CHF','KRW','CNY','TRY','HRK','NZD','THB','EUR','NOK','RUB','INR','MXN','CZK','BRL','PLN','PHP','ZAR']
 # IDR','BGN','ILS','GBP','DKK','CAD','JPY','HUF','RON','MYR','SEK','SGD','HKD','AUD','CHF','KRW','CNY','TRY','HRK','NZD','THB','EUR','NOK','RUB','INR','MXN','CZK','BRL','PLN','PHP','ZAR'
root.configure(background='#e6e5e5')
root.geometry("700x400")
 
Label_1 = Label(root, font=('lato black', 15, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=1, column=0, sticky=W)
label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\tКоличество:  \n\n", bg="#e6e5e5", fg="black")
label1.grid(row=2, column=0, sticky=W)
label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t  Из валюты:  \n\n\n", bg="#e6e5e5", fg="black")
label1.grid(row=3, column=0, sticky=W)
label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t  В валюту:  \n\n\n", bg="#e6e5e5", fg="black")
label1.grid(row=4, column=0, sticky=W)
label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t  Сумма конвертации:  \n\n", bg="#e6e5e5", fg="black")
label1.grid(row=8, column=0, sticky=W)
Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=5, column=0, sticky=W)
 
Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=7, column=0, sticky=W)
 
FromCurrency_option = tk.OptionMenu(root, variable1, *CurrenyCode_list)
ToCurrency_option = tk.OptionMenu(root, variable2, *CurrenyCode_list)
 
FromCurrency_option.grid(row=3, column=0, ipadx=45, sticky=E)
ToCurrency_option.grid(row=4, column=0, ipadx=45, sticky=E)
 
Amount1_field = tk.Entry(root)
Amount1_field.grid(row=2, column=0, ipadx=28, sticky=E)
 
Amount2_field = tk.Entry(root)
Amount2_field.grid(row=8, column=0, ipadx=31, sticky=E)
 
Label_9 = Button(root, font=('arial', 15, 'bold'), text="   Конвертировать  ", padx=2, pady=2, bg="lightblue", fg="white",
                 command=RealTimeCurrencyConversion)
Label_9.grid(row=6, column=0)
Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=9, column=0, sticky=W)
Label_9 = Button(root, font=('arial', 15, 'bold'), text="   Очистить все  ", padx=2, pady=2, bg="lightblue", fg="white",
                 command=clear_all)
Label_9.grid(row=10, column=0)
 
 
root.mainloop()