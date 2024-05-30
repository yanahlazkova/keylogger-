""" Создание экземпляров классов Listener и InputHistory.
Координация работы этих классов.
Обработка событий от пользователя (например, нажатия кнопок) """
import keyboard


import keyboard
class KeyLogger:
    def __init__(self):
        self.log = ""

    def run(self):
        """ Запуск приложения """
        print("Keylogger started. Press 'esc' to stop.")

        # Запуск обработки клавиатурных событий
        # keyboard.hook(self.handle_keyboard_event)
        events = keyboard.record('esc')
        keyboard.play(events)
        # keyboard.write(events)

        # Запуск обработки событий мыши
        # mouse_listener = mouse.Listener(
        #     on_move=self.handle_mouse_event,
        #     on_click=self.handle_mouse_event,
        #     on_scroll=self.handle_mouse_event)
        # mouse_listener.start()

        # Ждем нажатия клавиши Esc для завершения
        keyboard.wait('esc')
        # mouse_listener.stop()
        print("Keylogger stopped.")

    def handle_keyboard_event(self, event):
        """ Обработка события нажатия клавиши """
        # self.log = f'Key {event.name} {event.event_type}\n'
        self.log += event.name
        # print(f'Key {event.name} {event.event_type}')
        keyboard.play(event.name)

    def handle_mouse_event(self, *args):
        """ Обработка события от мыши """
        event_type = args[1] if len(args) > 1 else 'move'
        if event_type == 'move':
            x, y = args[0].x, args[0].y
            self.log += f'Mouse moved to ({x}, {y})\n'
            print(f'Mouse moved to ({x}, {y})')
        elif event_type == 'click':
            x, y = args[0].x, args[0].y
            button, pressed = args[1], args[2]
            action = 'pressed' if pressed else 'released'
            self.log += f'Mouse {action} at ({x}, {y}) with {button}\n'
            print(f'Mouse {action} at ({x}, {y}) with {button}')
        elif event_type == 'scroll':
            x, y = args[0].x, args[0].y
            dx, dy = args[1], args[2]
            self.log += f'Mouse scrolled at ({x}, {y}) by ({dx}, {dy})\n'
            print(f'Mouse scrolled at ({x}, {y}) by ({dx}, {dy})')