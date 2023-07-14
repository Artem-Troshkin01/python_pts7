import tkinter
from PIL import ImageTk, Image


def calculate():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())

        result = weight / (height ** 2)

        result_label.config(text=f'Индекс массы тела: {result:.2f}')
    except ValueError:
        result_label.config(text=f'Данные должны иметь числовой тип')


root = tkinter.Tk()  # Инициализация окна
root.title('Калькулятор веса')  # Название приложения

# Загрузка фон
background_image = Image.open('desktop-with-office-elements (1).jpg')
window_width = 800
window_height = 600

# Масштабирование изображения фона под размер окна
background_image = background_image.resize((window_width, window_height), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)
background_label = tkinter.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

root.geometry(f'{window_width}x{window_height}')  # Установка размеров окна в пикселях
root.resizable(False, False)

# Поле для ввода роста
height_label = tkinter.Label(root, text='Рост (м):', font=('Arial', 14), fg='black', bg='white')
height_label.place(relx=0.5, rely=0.4, anchor='center')  # Размещение подсказки для ввода

height_entry = tkinter.Entry(root, font=('Arial', 14))
height_entry.place(relx=0.5, rely=0.45, anchor='center')

# Поле для ввода веса
weight_label = tkinter.Label(root, text='Вес (кг)', font=('Arial', 14), fg='black', bg='white')
weight_label.place(relx=0.5, rely=0.5, anchor='center')

weight_entry = tkinter.Entry(root, font=('Arial', 14))
weight_entry.place(relx=0.5, rely=0.55, anchor='center')

# Кнопка для расчета веса
calculate_button = tkinter.Button(root, text='Рассчитать', font=('Arial', 14), command=calculate,
                                  bg='#4CAF50', fg='white', activebackground='#45A049', activeforeground='white')
calculate_button.place(relx=0.5, rely=0.65, anchor='center')

# Окно для вывода результатов
result_label = tkinter.Label(root, font=('Arial', 14), bg='white', fg='black')
result_label.place(relx=0.5, rely=0.75, anchor='center')

root.mainloop()
