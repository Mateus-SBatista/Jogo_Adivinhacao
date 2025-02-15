import random
import tkinter as tk
from tkinter import messagebox

# Função para iniciar o jogo
def iniciar_jogo():
    global numero_secreto, tentativas, limite_tentativas, inicio, fim

    try:
        inicio = int(entry_inicio.get())
        fim = int(entry_fim.get())
        if inicio >= fim:
            messagebox.showerror("Erro", "O início deve ser menor que o fim.")
            return
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")
        return

    numero_secreto = random.randint(inicio, fim)
    tentativas = 0
    limite_tentativas = 5
    label_status.config(text=f"Tente adivinhar o número entre {inicio} e {fim}.")
    label_tentativas.config(text=f"Tentativas restantes: {limite_tentativas}", fg="blue")
    button_palpite.config(state="normal")

# Função para verificar o palpite
def verificar_palpite():
    global tentativas

    try:
        palpite = int(entry_palpite.get())
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")
        return

    tentativas += 1
    tentativas_restantes = limite_tentativas - tentativas

    if palpite == numero_secreto:
        if tentativas == 1:
            messagebox.showinfo("Parabéns!", "Incrível! Você acertou de primeira! 🎉")
        else:
            messagebox.showinfo("Parabéns!", f"Você acertou em {tentativas} tentativa(s)!")
        resetar_jogo()
    elif tentativas >= limite_tentativas:
        messagebox.showinfo("Fim de Jogo", f"Que pena! Você usou todas as {limite_tentativas} tentativas. O número secreto era {numero_secreto}.")
        resetar_jogo()
    elif palpite < numero_secreto:
        label_status.config(text="Tente um número maior!", fg="green")
    else:
        label_status.config(text="Tente um número menor!", fg="red")

    if tentativas < limite_tentativas:
        label_tentativas.config(text=f"Tentativas restantes: {tentativas_restantes}")
    else:
        label_tentativas.config(text="Tentativas restantes: 0", fg="red")

# Função para resetar o jogo
def resetar_jogo():
    entry_inicio.delete(0, tk.END)
    entry_fim.delete(0, tk.END)
    entry_palpite.delete(0, tk.END)
    label_status.config(text="Configure o intervalo e clique em 'Iniciar Jogo'.", fg="black")
    label_tentativas.config(text="")
    button_palpite.config(state="disabled")

# Configuração da janela principal
root = tk.Tk()
root.title("Jogo de Adivinhação")
root.geometry("500x450")
root.configure(bg="#f0f8ff")  # Cor de fundo clara

# Estilo geral
font_title = ("Comic Sans MS", 18, "bold")
font_text = ("Comic Sans MS", 12)
font_button = ("Comic Sans MS", 12, "bold")

# Título
label_title = tk.Label(root, text="Jogo de Adivinhação 🎯", font=font_title, bg="#f0f8ff", fg="#2e8b57")
label_title.pack(pady=10)

# Widgets para configuração do intervalo
frame_config = tk.Frame(root, bg="#f0f8ff")
frame_config.pack(pady=10)

tk.Label(frame_config, text="Início do intervalo:", font=font_text, bg="#f0f8ff").grid(row=0, column=0, padx=5, pady=5)
entry_inicio = tk.Entry(frame_config, font=font_text, width=5)
entry_inicio.grid(row=0, column=1, padx=5)

tk.Label(frame_config, text="Fim do intervalo:", font=font_text, bg="#f0f8ff").grid(row=1, column=0, padx=5, pady=5)
entry_fim = tk.Entry(frame_config, font=font_text, width=5)
entry_fim.grid(row=1, column=1, padx=5)

button_iniciar = tk.Button(frame_config, text="Iniciar Jogo", font=font_button, bg="#ffcccb", fg="black", command=iniciar_jogo)
button_iniciar.grid(row=2, column=0, columnspan=2, pady=10)

# Status do jogo
label_status = tk.Label(root, text="Configure o intervalo e clique em 'Iniciar Jogo'.", font=font_text, bg="#f0f8ff", wraplength=400)
label_status.pack(pady=10)

# Exibição das tentativas restantes
label_tentativas = tk.Label(root, text="", font=font_text, bg="#f0f8ff")
label_tentativas.pack(pady=5)

# Widgets para palpites
frame_palpite = tk.Frame(root, bg="#f0f8ff")
frame_palpite.pack(pady=10)

tk.Label(frame_palpite, text="Seu palpite:", font=font_text, bg="#f0f8ff").grid(row=0, column=0, padx=5)
entry_palpite = tk.Entry(frame_palpite, font=font_text, width=5)
entry_palpite.grid(row=0, column=1, padx=5)

button_palpite = tk.Button(frame_palpite, text="Verificar Palpite", font=font_button, bg="#90ee90", fg="black", command=verificar_palpite, state="disabled")
button_palpite.grid(row=0, column=2, padx=5)

# Rodapé
label_footer = tk.Label(root, text="Boa sorte! Divirta-se! 😊", font=font_text, bg="#f0f8ff", fg="#4682b4")
label_footer.pack(pady=20)

# Iniciar o loop principal da interface
root.mainloop()
