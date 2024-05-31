"""  Класс для отслеживания событий клавиатуры и мыши.
Использует библиотеку keyboard для клавиатуры и pynput для мыши. """
import keyboard
from pynput import mouse

class Listener:
    def __init__(self):
        self.keyboard_hook = None
        # self.mouse_listener = None

    def start_listening(self, keyboard_callback): #, mouse_callback):
        """Запуск отслеживания нажатий клавиш и событий мыши"""
        self.keyboard_hook = keyboard.hook(keyboard_callback)

        # def on_move(x, y):
        #     mouse_callback('move', x, y)

        # def on_click(x, y, button, pressed):
        #     mouse_callback('click', x, y, button, pressed)
        #
        # def on_scroll(x, y, dx, dy):
        #     mouse_callback('scroll', x, y, (dx, dy))
        #
        # self.mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
        # self.mouse_listener.start()

    def stop_listening(self):
        """Остановка отслеживания нажатий клавиш и событий мыши"""
        if self.keyboard_hook:
            keyboard.unhook(self.keyboard_hook)
        # if self.mouse_listener:
        #     self.mouse_listener.stop()

    def get_pressed_keys(self):
        """Возвращает список нажатых клавиш в данный момент"""
        # Используем keyboard.is_pressed для проверки состояния каждой клавиши
        keys = [key for key in keyboard.all_modifiers if keyboard.is_pressed(key)]
        return keys
