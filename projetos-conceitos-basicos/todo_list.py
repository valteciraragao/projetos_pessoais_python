import tkinter as tk


# Função para adicionar tarefa
def add_task():
    task = entry.get()

    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)


# Função para remover tarefa
def remove_task():
    selected_task = listbox.curselection()

    if selected_task:
        listbox.delete(selected_task)


# Criação do janela principal
root = tk.Tk()
root.title("To-Do List App")
root.geometry("500x500")
root.resizable(False, False)


# Criação do janela tarefas
listbox = tk.Listbox(root, selectmode=tk.SINGLE)
listbox.pack(pady=10)

# Criação da label para inserir tarefas

entry = tk.Entry(root)
entry.pack(pady=5)

# Criação dos botões de adicionar e remover tarefas

add_button = tk.Button(root, text="Adicionar Tarefa", command=add_task)
remove_button = tk.Button(root, text="Remover Tarefa", command=remove_task)
add_button.pack()
remove_button.pack()

root.mainloop()