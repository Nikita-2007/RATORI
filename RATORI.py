#RATORI-game

__autor__ = "Nikita"

from modules.Main import Main
from pyautogui import *

game_version = 1 # Запрос версии с интернета
if __name__ == '__main__':
    main = Main()
    local_version = main.local_version
    if local_version < game_version:
        print("Данная версия игры усторела, нужно обновить")
        alert("Данная версия игры усторела, нужно обновить", "Обновление", button = "Ok")
    else:
        main.game_start()