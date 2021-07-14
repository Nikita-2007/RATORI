import shelve


class Save(object):
    """Сохранение и загрузка"""
    def __init__(self):
        """Конструктор"""
        path = "save/save_00"
        self.file = shelve.open(path)
        self.value = 5 # Временно

    def __del__(self):
        self.file.close()

    def save_data(self, value):
        self.value = value
        self.file.data = self.value
        print("Сохранения")

    def load_data(self):
        self.file.data = self.value
        print("Загрузка")
        return(self.value)