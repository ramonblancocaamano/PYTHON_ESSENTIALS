#pip install --upgrade pymupdf

import os
import fitz

def get_text_from_pdf(file, format='text'):
    text = []
    if (not os.path.isfile(file)):
        return text
    with fitz.open(file) as pdf:
        try:
            for page in pdf:
                try:
                    texto = page.get_text(format)
                    print(texto)
                    text.append(texto)
                except:
                    text.append('\n' + '----- Pagina sin texto extraido -----' + '\n')
        except:
            pass
    return text

def save_text_file(file, text, encoding='utf-8'):
    with open(file, 'w', encoding=encoding) as save:
        save.write(text)

def extract_text_from_pdf(source_file, target_file):
    text = ' '.join(get_text_from_pdf(source_file))
    save_text_file(target_file, text)


file = r'C:\datasets\pdf\BOE-N-2024-651175.pdf'
extract_text_from_pdf(file, f'{file}.txt')

print("Fin de la aplicacion")

