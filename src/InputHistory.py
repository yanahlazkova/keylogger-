""" Класс для сохранения и загрузки истории ввода.
Он сохраняет каждое событие в текстовый файл и загружает его
при запуске"""

class InputHistory:
    def __init__(self):
        self.history_file = "input_history.txt"
        self.history = self.load_input()

    def save_input(self, text):
        """Сохранение введенного текста в истории"""
        with open(self.history_file, 'a') as file:
            file.write(text + '\n')
        self.history.append(text)

    def load_input(self):
        """Загрузка истории ввода"""
        try:
            with open(self.history_file, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            return []

    def get_input_history(self):
        """Возвращение списка записей истории ввода"""
        return self.history