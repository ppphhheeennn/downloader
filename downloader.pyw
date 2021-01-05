import wget
import tkinter as tk
def dwnld():
    url = url1.get()
    name = name1.get()
    wget.download(url, name)

window = tk.Tk()
window.title("Загрузчик")
window.geometry("200x112")
window.resizable(0, 0)
lbl = tk.Label(text="Введите ссылку для загрузки:")
lbl1 = tk.Label(text="Введите расширение файла:")
url1 = tk.Entry()
name1 = tk.Entry()
lbl.pack()
url1.pack()
lbl1.pack()
name1.pack()
button = tk.Button(text="Загрузить!", command=dwnld)
button.pack()
window.mainloop()
