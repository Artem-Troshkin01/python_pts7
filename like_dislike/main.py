import tkinter
from PIL import ImageTk, Image
import os

# Абсолютный путь к скрипту
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # /home/artem/PycharmProjects/ITeen/ArtemTroshkin/like_dislike


def like():
    """Обработка нажатия на кнопку лайк

    :return:
    """
    global total_likes, likes_label, current_image_index
    total_likes += 1
    likes_label.config(text=f'Лайков: {total_likes}')
    current_image_index = (current_image_index + 1) % len(images_filenames)
    update_image()


def dislike():
    """Обработка нажатия на кнопку дизлайк

    :return:
    """
    global total_dislikes, dislikes_label, current_image_index
    total_dislikes += 1
    dislikes_label.config(text=f'Дизлайков: {total_dislikes}')
    current_image_index = (current_image_index + 1) % len(images_filenames)
    update_image()


def update_image():
    """Обновление изображения

    :return:
    """
    # Путь к конкретному изображению
    image_path = os.path.join(image_directory, images_filenames[current_image_index])

    # Масштабирование полученного изображения и отображение
    image = Image.open(image_path)
    image = image.resize((300, 200), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    image_label.config(image=photo)
    image_label.image = photo


total_likes = 0
total_dislikes = 0
current_image_index = 0  # Индекс пути к фотографии

image_directory = os.path.join(BASE_DIR, 'images')  # Абсолютный путь к папке с изображениями
images_filenames = sorted(os.listdir(image_directory))  # Список с изображениями

root = tkinter.Tk()
root.title('Лайк-дизлайк')
root.geometry('400x450')
root.resizable(False, False)

# Путь к конкретному изображению
image_path = os.path.join(image_directory, images_filenames[current_image_index])

# Масштабирование полученного изображения и отображение
image = Image.open(image_path)
image = image.resize((300, 200), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

image_label = tkinter.Label(root, image=photo)
image_label.pack(pady=10)

# Добавляем изображения лайка и дизлайка
like_image = Image.open(os.path.join(BASE_DIR, 'like.png'))
dislike_image = Image.open(os.path.join(BASE_DIR, 'dislike.png'))

# Масштабирование изображений
like_image = like_image.resize((100, 100), Image.LANCZOS)
dislike_image = dislike_image.resize((100, 100), Image.LANCZOS)

like_image = ImageTk.PhotoImage(like_image)
dislike_image = ImageTk.PhotoImage(dislike_image)

# Создаем фрейм для кнопок
buttons_frame = tkinter.Frame(root)
buttons_frame.pack(pady=20)

# Создаем и размещаем кнопку лайк
like_button = tkinter.Button(buttons_frame, image=like_image, bd=0, command=like)
like_button.pack(side=tkinter.LEFT, padx=10)

# Создаем и размещаем кнопку дизлайк
dislike_button = tkinter.Button(buttons_frame, image=dislike_image, bd=0, command=dislike)
dislike_button.pack(side=tkinter.RIGHT, padx=10)

# Создаем контейнер для кол-ва лайков
likes_label = tkinter.Label(root, text='Лайков: 0', font=('Arial', 14))
likes_label.pack()

# Создаем контейнер для кол-ва дизлайков
dislikes_label = tkinter.Label(root, text='Дизлайков: 0', font=('Arial', 14))
dislikes_label.pack()

root.mainloop()
