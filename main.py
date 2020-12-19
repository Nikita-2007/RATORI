#RATORI-game
from modules import game
#from pyautogui import *
game_version = 1 # Запрос версии с интернета

if __name__ == '__main__':
    local_version = game.local_version
    if local_version < game_version:
        print("Данная версия игры усторела, нужно обновить")
#        alert("Данная версия игры усторела, нужно обновить", "Обновление", button = "Ok")
    else:
        game.game_cycle()