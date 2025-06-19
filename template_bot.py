import pyautogui
import time

# Lista de cliques (será substituída pelo gerador)
cliques = "__CLIQUES__"  # com dois underlines de cada lado (certo)

print("Bot iniciando em 5 segundos...")
time.sleep(5)

for acao in cliques:
    time.sleep(acao["delay"])
    pyautogui.moveTo(acao["x"], acao["y"])
    pyautogui.click()
