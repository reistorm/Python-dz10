from tkinter import *
import requests

root = Tk()
root.geometry("500x500")
root.resizable(0, 0)
root.title("Конвертер валют")

Label(root, text="Конвертер валют", bg='blue', font='Arial 12 bold').pack()

var1 = StringVar(root)
var2 = StringVar(root)
cost = StringVar(root)
currency_list = ['USD', 'EUR', 'RUB']

Label(root, text="Выберите валюту: ", font='Arial 12 bold').place(x=150, y=100)
OptionMenu(root, var1, *currency_list).place(x=300, y=100)

Label(root, text="Выберите валюту: ", font='Arial 12 bold').place(x=150, y=200)
Entry(root, width=10, textvariable=cost).place(x=200, y=240)
OptionMenu(root, var2, *currency_list).place(x=300, y=200)

def get_currency():
    curs1 = var1.get()
    curs2 = var2.get()
    multi = cost.get()

    token = "NL53LCD20PA73OMO"
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={curs1}&to_currency={curs2}&apikey={token}'
    r = requests.get(url)
    data = r.json()
    val1 = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    result = val1 * float(multi)
    Label(root, text=f"{result}", font='arial 12 bold').place(x=300, y = 300)


Button(root, text="Конвертировать", font='Arial 15 bold', bg='red', command=get_currency).place(x=150, y=300)

root.mainloop()
