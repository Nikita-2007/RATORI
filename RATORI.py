#RATORI-game
from modules.Main import Main
from pyautogui import *
game_version = 1 # Запрос версии с интернета
main = Main()
if __name__ == '__main__':
    local_version = main.local_version
    if local_version < game_version:
        print("Данная версия игры усторела, нужно обновить")
        alert("Данная версия игры усторела, нужно обновить", "Обновление", button = "Ok")
    else:
        main.game_cycle()