import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox
from PIL import Image
import analiz

background = ""
color = ""
file_path = ""
png_name = "wordcloud.png"

def show_color_picker():
    global color
    color = colorchooser.askcolor(title="Выберите цвет")
    if color and len(color) == 2 and color[1]:
        print("Выбранный цвет:", color[1])
        update_canvas_color()

def update_canvas_color():
    if color and len(color) == 2 and color[1]:
        canvas.config(bg=color[1])

def select_file():
    global file_path
    file_path = filedialog.askopenfilename(title="Выберите файл")
    if file_path:
        print("Выбранный файл:", file_path)

def open_image():
    global png_name
    if png_name:
        image = Image.open(png_name)
        image.show()

def run():

    pos_list = []
    if noun_var.get():
        pos_list.append('NOUN')
    if verb_var.get():
        pos_list.append('VERB')


    if file_path:
        if color and len(color) == 2 and color[1]:
            analiz.TextAnalyser(
                file_name=file_path,
                pos_list=pos_list,
                chislo=int(entry.get()),
                background=color[1],
                width=int(entry2.get()),
                height=int(entry3.get())
            )
        if not background:
            messagebox.showerror("Ошибка", "Выберите цвет перед запуском анализатора")
        
        if not file_path:
            messagebox.showerror("Ошибка", "Выберите файл перед запуском анализатора")

window = tk.Tk()
window.title("Анализатор текста:")

# Создание и упорядочивание виджетов с помощью grid()
label = tk.Label(window, text="Кол-во слов для вордклауд:", font=("Impact", 20), background="#ffcc00")
label.grid(row=0, column=0, padx=6, pady=6)

entry = tk.Entry(window, font=("Arial black", 18))
entry.grid(row=1, column=0, padx=6, pady=6)
entry.insert(0, "10")

file_button = tk.Button(window, font=("Impact", 17), background="#59c977", text="выбрать файл", command=select_file)
file_button.grid(row=2, column=0, padx=6, pady=6)

button = tk.Button(window, font=("Impact", 17), background="#DAA520", text="сделать вордклауд", command=run)
button.grid(row=4, column=0, padx=6, pady=6)

button2 = tk.Button(window, font=("Impact", 17), background="#59c977", text="выбрать цвет", command=show_color_picker)
button2.grid(row=3, column=0, padx=6, pady=6)

label2 = tk.Label(window, text="Ширина:", font=("Impact", 19))
label2.grid(row=0, column=1, padx=6, pady=6)

entry2 = tk.Entry(window, font=("Impact", 18))
entry2.grid(row=1, column=1, padx=6, pady=6)
entry2.insert(0, "1000")

label3 = tk.Label(window, text="Высота:", font=("Impact", 19))
label3.grid(row=2, column=1, padx=6, pady=6)

canvas = tk.Canvas(window, width=500, height=40, bg="#59c977")
canvas.grid(row=6, column=0, columnspan=2, padx=6, pady=6)

entry3 = tk.Entry(window, font=("Impact", 18))
entry3.grid(row=3, column=1, padx=6, pady=6)
entry3.insert(0, "800")

noun_var = tk.BooleanVar()  
cb_noun = tk.Checkbutton(window, text="Включить Noun(Сущ)", font=("Impact", 19), variable=noun_var)
cb_noun.grid(row=4, column=1, padx=6, pady=6)

verb_var = tk.BooleanVar()  
cb_verb = tk.Checkbutton(window, text="Включить Verb(Гл)", font=("Impact", 19), variable=verb_var)
cb_verb.grid(row=5, column=1, padx=6, pady=6)

imButton = tk.Button(window, text="Открыть png", font=("Impact", 19), background="#ffcc00", command=open_image)
imButton.grid(row=5, column=0, padx=6, pady=6)

window.mainloop()