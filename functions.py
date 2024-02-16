import re
import os
import PyPDF2


def extract_date_from_filename(filename):
    # Use a breakpoint in the code line below to debug your script.
    pattern = r'\d{4}-\d{2}-\d{2}'
    match = re.search(pattern, filename)  # classe Macth
    if match:
        return match.group()


def sorting_files_by_date(directory_path):
    files = [f for f in os.listdir(directory_path)
             if os.path.isfile(os.path.join(directory_path, f))]

    # var lista de tuplas
    pdf_files_with_date = []

    for file in files:
        if file.lower().endswith('.pdf'):
            date = extract_date_from_filename(file)
            if date:
                # tupla: (filename, data_padrao)
                pdf_files_with_date.append((file, date))

    return sorted(pdf_files_with_date, key=lambda x: x[1])


def merge_pdfs_sorted_by_date(directory_path, output_file='mesclados.pdf'):

    pdf_files_sorted_by_date = sorting_files_by_date(directory_path)
    merger = PyPDF2.PdfMerger()

    for file, _ in pdf_files_sorted_by_date:
        file_path = os.path.join(directory_path, file)
        merger.append(file_path)

    new_path = '/'.join(['arquivos_mesclados', directory_path.split('/')[1]])
    if not os.path.exists(new_path):
        os.makedirs(new_path)

    output_path = os.path.join(new_path, output_file)
    with open(output_path, 'wb') as output:
        merger.write(output)

    print(f'Arquivos PDF foram mesclados e salvo como {output_file} em {new_path}')
