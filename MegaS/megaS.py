import random
import tkinter as tk
from tkinter import messagebox

#Números mais sorteados (quentes) e suas frequências
numeros_mais = [10, 53, 5, 34, 37, 33, 38, 17, 32, 43]
frequencias_mais = [338, 330, 318, 314, 311, 309, 308, 306, 306, 306]

#Números menos sorteados (frios) e suas frequências
numeros_menos = [26, 21, 55]
frequencias_menos = [237, 240, 249]

#Combinar listas e pesos
numeros = numeros_mais + numeros_menos
pesos = frequencias_mais + frequencias_menos

def gerar_aposta_equilibrada(numeros, pesos, tamanho=6):
    aposta = set()
    while len(aposta) < tamanho:
        numero = random.choices(numeros, weights=pesos, k=1)[0]
        aposta.add(numero)
    return sorted(aposta)

def gerar_apostas():
    apostas_text.delete("1.0", tk.END)
    try:
        qtd = int(entry_qtd.get())
        for i in range(qtd):
            aposta = gerar_aposta_equilibrada(numeros, pesos)
            apostas_text.insert(tk.END, f"Aposta {i+1}: {aposta}\n")
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido de apostas.")

#Interface
janela = tk.Tk()
janela.title("Gerador MegaS")
janela.geometry("400x300")
janela.resizable(False, False)

#Widgets
label_title = tk.Label(janela, text="Gerar números", font=("Arial", 14))
label_title.pack(pady=10)

entry_qtd = tk.Entry(janela, width=10, font=("Arial", 12))
entry_qtd.pack()
entry_qtd.insert(0, "5")

btn_gerar = tk.Button(janela, text="Gerar", command=gerar_apostas, font=("Arial", 12))
btn_gerar.pack(pady=10)

apostas_text = tk.Text(janela, height=10, width=45, font=("Courier", 10))
apostas_text.pack()

#Iniciar
janela.mainloop()
