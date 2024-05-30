""" Отображение введенного текста в пользовательском интерфейсе """

class TextDisplay:
    def __init__(self, text) -> None:
        self.text = text
        
    
    def display_text(self):
        print(self.text)