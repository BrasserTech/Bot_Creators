import pyautogui
import time
import json

def gravar_cliques():
    cliques = []

    print("Posicione o mouse. A gravação começa em 3 segundos...")
    time.sleep(3)

    print("Gravando... Pressione Ctrl+C para encerrar.")
    try:
        while True:
            x, y = pyautogui.position()
            cliques.append({
                "x": x,
                "y": y,
                "delay": 1  # segundos entre cada clique (ajuste se quiser)
            })
            print(f"Capturado: x={x}, y={y}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Gravação encerrada.")

    with open("scripts_salvos/exemplo.json", "w") as f:
        json.dump(cliques, f, indent=2)
        print("Cliques salvos em 'scripts_salvos/exemplo.json'.")

if __name__ == "__main__":
    gravar_cliques()
