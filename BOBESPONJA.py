import tkinter as tk
from PIL import Image, ImageTk
import os

# URL da imagem
image_url = "https://i.ytimg.com/vi/XqdEgUp7fO0/maxresdefault.jpg"
image_path = "maxresdefault.jpg"  # Nome do arquivo para salvar a imagem

# Baixa a imagem usando curl
os.system(f"curl -o {image_path} {image_url}")  # Para Windows, use curl
# os.system(f"wget {image_url}")  # Para sistemas Linux, você pode usar wget

def open_new_window():
    new_window = tk.Toplevel()
    new_window.attributes('-fullscreen', True)
    new_window.attributes('-topmost', True)  # Mantém a nova janela sempre no topo
    new_window.bind("<Alt-F4>", lambda e: open_new_window())

    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    label = tk.Label(new_window, image=photo)
    label.image = photo  # Mantém uma referência da imagem
    label.pack()

    new_window.protocol("WM_DELETE_WINDOW", lambda: new_window.destroy())

def on_closing():
    pass

# Cria a janela principal
root = tk.Tk()
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)  # Mantém a janela principal sempre no topo
root.bind("<Alt-F4>", lambda e: open_new_window())

# Carrega a imagem localmente
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

label = tk.Label(root, image=photo)
label.image = photo  # Mantém uma referência da imagem
label.pack()

root.protocol("WM_DELETE_WINDOW", on_closing)

# Inicia a primeira janela
open_new_window()
root.mainloop()
