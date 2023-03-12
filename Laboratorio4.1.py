"""
Лабораторная работа №4
Вариант №2.
Вводная часть: нет
Формат ключа: XXXX-XXXX-XXXX-XXXX
Правило генерации: Каждый блок имеет одну цифру и три буквы в случайном порядке
"""
import string

from random import choices, sample

import tkinter as tk

# Для отключения приветственного сообщения
import contextlib
with contextlib.redirect_stdout(None):
    import pygame

from PIL import Image, ImageTk


def set_text(text):
    """
    Функция замена текста в поле
    :param text: Текст
    :return:     None
    """
    e.delete(0, tk.END)
    e.insert(0, text)


def generate_key():
    """
    Функция генерации ключа по заданию
    :return: Ключ
    """
    # Зададим возможные варианты
    alphabet = string.ascii_uppercase
    digits = string.digits

    # Сгенерируем ключ
    key = "-".join(
        [
            "".join(sample(choices(alphabet, k=3) + choices(digits, k=1), 4))
            for _ in range(4)
        ]
    )
    return key


# Создание главного окна
window = tk.Tk()
window.title("Key generator")
window.geometry("683x384")

# Иконка приложения
ico = Image.open("icon.ico")
photo = ImageTk.PhotoImage(ico)
window.wm_iconphoto(False, photo)

# Картинка для фона
background_image = tk.PhotoImage(file="modern warfare.jpg")
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(window, bg=None)
frame.place(relx=0.5, rely=0.5, anchor="center")


e = tk.Entry(frame, width=23)
e.pack()

# Кнопка генерации ключа
b1 = tk.Button(frame, width=19, text="Generate!", bg="#9cc", command=lambda: set_text(generate_key()))
b1.pack()

# Запуск музыки
pygame.init()
pygame.mixer.music.load("sound.mp3")  # Loading File Into Mixer
pygame.mixer.music.play()  # Playing It In The Whole Device

# Вывод окна
window.mainloop()