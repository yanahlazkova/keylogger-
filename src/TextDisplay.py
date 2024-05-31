""" Отображение введенного текста в пользовательском интерфейсе """

class TextDisplay:
    # def __init__(self):
    #     self.text = None

    
    def display_text(self):
        try:
            with open('input_history.txt', 'r') as file:
                text = file.read()
                print(text)
        except FileNotFoundError as e:
            print(e)


# class TextDisplay:
#     def display_text(self, text):
#         """Отображение текста в пользовательском интерфейсе"""
#         print(f'Display: {text}')

