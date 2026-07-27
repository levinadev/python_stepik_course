"""
Дан словарь: settings = {"volume": 50, "brightness": 70}.
Используя метод .update(), добавьте в него пары из словаря new_settings = {"contrast": 80, "volume": 60} (обратите внимание — ключ "volume" перезапишется).
Выведите итоговый словарь.
"""

settings = {"volume": 50, "brightness": 70}
new_settings = {"contrast": 80, "volume": 60}
settings.update(new_settings)
print(settings)
