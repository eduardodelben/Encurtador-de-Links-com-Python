import tkinter as tk
import pyshorteners
import pyperclip

def encurtar():
    encurtador = pyshorteners.Shortener()
    link_encurtado = encurtador.tinyurl.short(link_longo_entrada.get())
    link_curto_saida.insert(0, link_encurtado)

def copiar():
    link = link_curto_saida.get()
    if link:
        pyperclip.copy(link)
        copiar_botao.config(text="Copiado!", bg="#4CAF50") 

janela = tk.Tk()
janela.title("Encurtador de link")
janela.geometry("700x400")
janela.config(bg="#1e1e1e") 
frame = tk.Frame(janela, bg="#f0f0f0")
frame.pack(pady=20, padx=20)

link_longo = tk.Label(janela, text="Link Longo Aqui:")
link_longo_entrada = tk.Entry(janela, width=50, font=("Arial", 12)) 
link_curto = tk.Label(janela, text="Link Encurtado:")
link_curto_saida = tk.Entry(janela, width=50, font=("Arial", 12))

link_botao = tk.Button(janela, text="Encurtar", font=("Arial", 12), fg="white", bg="#007acc", padx=10, pady=5, width=30, height=1, borderwidth=3, command=encurtar)

copiar_botao = tk.Button(frame, text="Copiar", font=("Arial", 12), fg="white", bg="#555", padx=15, pady=5, command=copiar)

link_longo.config(bg="#1e1e1e", fg="white")
link_curto.config(bg="#1e1e1e", fg="white")

link_longo.pack(pady=5)
link_longo_entrada.pack(pady=5)
link_curto.pack(pady=5)
link_curto_saida.pack(pady=5)
link_botao.pack(pady=10)
copiar_botao.pack(pady=5)

janela.mainloop()