from customtkinter import *
import random

def generate_password():
    length = 6
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{};:,.<>/?"
    password = "".join(random.choice(characters) for _ in range(length))

    result_field.delete(0, "end")
    result_field.insert(0, password)

# Вікно
window = CTk()
window.geometry("400x250")
window.title("Генератор паролів")

# Поле для відображення пароля
result_field = CTkEntry(window, height=40, width=300, font=("Arial", 16))
result_field.pack(pady=20)

# Кнопка генерації
generate_btn = CTkButton(window, text="Згенерувати пароль", command=generate_password)
generate_btn.pack(pady=20)

window.mainloop()
