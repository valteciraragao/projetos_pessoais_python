import tkinter as tk
from tkinter import filedialog, messagebox

import PyPDF2
from deep_translator import GoogleTranslator
from fpdf import FPDF


def upload_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        entry_file_path.delete(0, tk.END)
        entry_file_path.insert(0, file_path)

def translate_pdf():
    file_path = entry_file_path.get()
    if not file_path:
        messagebox.showerror("Erro", "Por favor, selecione um arquivo PDF.")
        return

    translator = GoogleTranslator(source='en', target='pt')

    # Leitura do PDF
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        translated_text = ""

        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text = page.extract_text()
            # Tradução do texto
            translated = translator.translate(text)
            translated_text += translated + "\n"

    # Salvar PDF traduzido
    save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if save_path:
        pdf = FPDF()
        pdf.add_page()
        # Usar fonte que suporta Unicode
        pdf.add_font("DejaVu", "", "/usr/share/fonts/TTF/DejaVuSans.ttf", uni=True)
        pdf.set_font("DejaVu", size=12)
        pdf.multi_cell(0, 10, translated_text)
        pdf.output(save_path)
        messagebox.showinfo("Sucesso", "PDF traduzido e salvo com sucesso!")

# Interface Gráfica
root = tk.Tk()
root.title("Tradutor de PDF")
root.geometry("400x200")

# Campo para o caminho do arquivo
entry_file_path = tk.Entry(root, width=40)
entry_file_path.pack(pady=10)

# Botão para upload do arquivo
btn_upload = tk.Button(root, text="Upload PDF", command=upload_pdf)
btn_upload.pack(pady=5)

# Botão para traduzir
btn_translate = tk.Button(root, text="Traduzir e Salvar PDF", command=translate_pdf)
btn_translate.pack(pady=20)

root.mainloop()

root.mainloop()
