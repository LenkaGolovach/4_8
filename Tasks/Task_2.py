import tkinter as tk

def update_text_size(event=None):
    """Обновление размеров многострочного текстового поля"""
    try:
        # Получаем значения ширины и высоты из текстовых полей
        new_width = int(width_entry.get())
        new_height = int(height_entry.get())
        # Применяем новые размеры к многострочному текстовому полю
        text_widget.config(width=new_width, height=new_height)
    except ValueError:
        # Обработка случая, когда в поля введены нечисловые значения
        print("Пожалуйста, введите числовые значения для размеров.")

def on_focus_in(event):
    """Изменение фона на белый при получении фокуса"""
    event.widget.config(bg='white')

def on_focus_out(event):
    """Изменение фона на светло-серый при потере фокуса"""
    event.widget.config(bg='lightgrey')

# Создание главного окна приложения
root = tk.Tk()
root.title("Изменение размера текстового поля")

# Создание и расположение виджетов для ввода ширины и высоты
width_label = tk.Label(root, text="Ширина:")
width_label.pack(side=tk.LEFT)
width_entry = tk.Entry(root)
width_entry.pack(side=tk.LEFT)

height_label = tk.Label(root, text="Высота:")
height_label.pack(side=tk.LEFT)
height_entry = tk.Entry(root)
height_entry.pack(side=tk.LEFT)

# Создание кнопки для изменения размера
update_button = tk.Button(root, text="Изменить размер", command=update_text_size)
update_button.pack(side=tk.LEFT)

# Создание многострочного текстового поля
text_widget = tk.Text(root, width=50, height=10, bg='lightgrey')
text_widget.pack(padx=10, pady=10)

# Привязка событий фокуса к многострочному текстовому полю
text_widget.bind("<FocusIn>", on_focus_in)
text_widget.bind("<FocusOut>", on_focus_out)

# Привязка события нажатия клавиши Enter к обновлению размера
root.bind("<Return>", update_text_size)

# Запуск главного цикла приложения
root.mainloop()
