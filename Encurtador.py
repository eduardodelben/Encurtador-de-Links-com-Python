import tkinter as tk
import pyshorteners

def encurtar():
    encurtador = pyshorteners.Shortener()
    link_encurtado = encurtador.tinyurl.short(link_longo_entrada.get())
    link_curto_saida.insert(0, link_encurtado)

janela = tk.Tk()
janela.title("Encurtador de link")
janela.geometry("700x400")

link_longo = tk.Label(janela, text="Link Longo Aqui:")
link_longo_entrada = tk.Entry(janela, width=50, font=("Arial", 12)) 
link_curto = tk.Label(janela, text="Link Encurtado:")
link_curto_saida = tk.Entry(janela, width=50, font=("Arial", 12))
link_botao = tk.Button(janela, text="Encurtar", font=("Arial", 12), fg="white", bg="#007acc", padx=10, pady=5, width=30, height=1, borderwidth=3, command=encurtar)

link_longo.pack(pady=10)
link_longo_entrada.pack(pady=10)
link_curto.pack(pady=10)
link_curto_saida.pack(pady=10)
link_botao.pack(pady=10)

janela.mainloop()