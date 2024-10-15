import subprocess
import time
import random
import win32gui
import win32api

art_text = """
░░░░█─────────────█▀─▀──
░░░░▓█───────▄▄▀▀█──────
░░░░▒░█────▄█▒░░▄░█─────
░░░░░░░▀▄─▄▀▒▀▀▀▄▄▀─────
░░░░░░░░░█▒░░░░▄▀───────
▒▒▒░░░░▄▀▒░░░░▄▀────────
▓▓▓▓▒░█▒░░░░░█▄─────────
█████▀▒░░░░░█░▀▄────────
█████▒▒░░░▒█░░░▀▄───────
███▓▓▒▒▒▀▀▀█▄░░░░█──────
▓██▓▒▒▒▒▒▒▒▒▒█░░░░█─────
▓▓█▓▒▒▒▒▒▒▓▒▒█░░░░░█────
░▒▒▀▀▄▄▄▄█▄▄▀░░░░░░░█───
"""

while True:
    with open("troll.txt", "w", encoding="utf-8") as f:
        f.write(art_text)

    proc = subprocess.Popen(["notepad.exe", "troll.txt"])
    
    # Espera um pouco para a janela abrir
    time.sleep(0.1)

    # Obter a handle da janela do Notepad
    hwnd = win32gui.FindWindow(None, "troll.txt - Notepad")
    
    if hwnd:
        # Gera coordenadas aleatórias dentro de uma tela padrão
        x = random.randint(0, win32api.GetSystemMetrics(0) - 300)  # Largura - largura da janela
        y = random.randint(0, win32api.GetSystemMetrics(1) - 300)  # Altura - altura da janela
        win32gui.MoveWindow(hwnd, x, y, 300, 300, True)  # Move a janela
    time.sleep(0)
