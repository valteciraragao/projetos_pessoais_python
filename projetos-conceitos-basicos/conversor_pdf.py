import os
import tkinter as tk
from tkinter import filedialog, messagebox

import fitz  # PyMuPDF
from bs4 import BeautifulSoup
from ebooklib import ITEM_DOCUMENT, epub


# Função para converter EPUB para PDF
def epub_to_pdf(epub_path, pdf_path):
    book = epub.read_epub(epub_path)
    pdf_document = fitz.open()

    for item in book.get_items_of_type(ITEM_DOCUMENT):
        soup = BeautifulSoup(item.get_body_content(), 'html.parser')
        text = soup.get_text()
        pdf_document.insert_page(-1, text=text)
    
    pdf_document.save(pdf_path)
    pdf_document.close()
    messagebox.showinfo("Sucesso", "EPUB convertido para PDF com sucesso!")

# Função para converter AZW3 para PDF usando calibre
def azw3_to_pdf(azw3_path, pdf_path):
    os.system(f'ebook-convert "{azw3_path}" "{pdf_path}"')
    messagebox.showinfo("Sucesso", "AZW3 convertido para PDF com sucesso!")

# Função para escolher o arquivo
def choose_file():
    file_path = filedialog.askopenfilename(filetypes=[("eBooks", "*.epub *.azw3")])
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

# Função para escolher onde salvar o arquivo
def choose_save_location():
    save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if save_path:
        save_entry.delete(0, tk.END)
        save_entry.insert(0, save_path)

# Função para iniciar a conversão
def convert():
    file_path = file_entry.get()
    save_path = save_entry.get()
    
    if not file_path or not save_path:
        messagebox.showwarning("Aviso", "Por favor, selecione um arquivo e um local para salvar.")
        return
    
    if file_path.endswith(".epub"):
        try:
            epub_to_pdf(file_path, save_path)
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao converter EPUB para PDF: {e}")
    elif file_path.endswith(".azw3"):
        try:
            azw3_to_pdf(file_path, save_path)
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao converter AZW3 para PDF: {e}")
    else:
        messagebox.showerror("Erro", "Formato de arquivo não suportado.")

# Criação da interface gráfica
root = tk.Tk()
root.title("Conversor de eBooks para PDF")

file_label = tk.Label(root, text="Selecione o arquivo:")
file_label.pack(pady=5)
file_entry = tk.Entry(root, width=50)
file_entry.pack(pady=5)
file_button = tk.Button(root, text="Escolher arquivo", command=choose_file)
file_button.pack(pady=5)

save_label = tk.Label(root, text="Selecione onde salvar:")
save_label.pack(pady=5)
save_entry = tk.Entry(root, width=50)
save_entry.pack(pady=5)
save_button = tk.Button(root, text="Escolher local", command=choose_save_location)
save_button.pack(pady=5)

convert_button = tk.Button(root, text="Converter", command=convert)
convert_button.pack(pady=20)

root.mainloop()

root.mainloop()
