import random
import tkinter
from tkinter import messagebox
from PIL import ImageTk, Image


def generate_secret_number():
    """Генерирует случайное число

    :return: рандомное число от 1 до 100
    """
    return random.randint(1, 100)


def check_guess(secret_number, guess):
    """Проверка введенного числа

    :param secret_number: загаданное число
    :param guess: введенное число
    :return: результат
    """
    global guesses_taken
    if guess < secret_number:
        guesses_taken += 1
        return 'Холодно'
    elif guess > secret_number:
        guesses_taken += 1
        return 'Горячо'
    else:
        return 'Победа!'


def check_button():
    """Обработка нажатия на кнопку

    :return:
    """
    guess = int(entry.get())
    result = check_guess(secret_number=secret_number, guess=guess)
    result_label.config(text=result)

    if result == 'Победа!':
        message = f'Вы угадали число за {guesses_taken} попыток!'
        messagebox.showinfo(title='Победа!', message=message)
        root.destroy()  # Отключение основного окна


root = tkinter.Tk()
root.title('Холодно-горячо')

background_image = Image.open('26539479_7234325.jpg')

window_width, window_height = 800, 600

background_image = background_image.resize((window_width, window_height), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)
background_label = tkinter.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

root.geometry(f'{window_width}x{window_height}')
root.resizable(False, False)  # Запрет масштабирования

# Создание виджета-инструкции
instruction_label = tkinter.Label(root, text='Я загадал число от 1 до 100. Попробуй его угадать',
                                  font=('Arial', 18), bg='white')
instruction_label.place(relx=0.5, rely=0.4, anchor='center')

# Поле для ввода числа
entry = tkinter.Entry(root, font=('Arial', 15))
entry.place(relx=0.5, rely=0.5, anchor='center')

check_button = tkinter.Button(root, text='Проверить', font=('Arial', 15),
                              bg='#4CAF50', fg='white', activebackground='#45A049',
                              activeforeground='white', command=check_button)
check_button.place(relx=0.5, rely=0.6, anchor='center')

# Поле для результата
result_label = tkinter.Label(root, font=('Arial', 15), fg='black', bg='white')
result_label.place(relx=0.5, rely=0.7, anchor='center')

# Инициализация переменных
secret_number = generate_secret_number()  # Случайное число
guesses_taken = 0  # Кол-во попыток

root.mainloop()

# def play_game():
#     """Запуск игры
#
#     :return:
#     """
#     secret_number = generate_secret_number()  # Случайное число
#     guesses_taken = 0  # Кол-во попыток
#
#     print('Я загадал число от 1 до 100. Попробуйте отгадать его')
#
#     while True:
#         guess = int(input('Введите ваше число: '))
#         guesses_taken += 1
#
#         result = check_guess(secret_number=secret_number, guess=guess)
#         print(result)
#
#         if result == 'Победа!':
#             print(f'Вы угадали число за {guesses_taken} попыток')
#             break
#
#
# if __name__ == '__main__':
#     play_game()
