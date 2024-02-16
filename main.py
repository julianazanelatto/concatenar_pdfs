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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    result = extract_date_from_filename('Proposta de Consultoria em Análise de Currículo e Direcionam 2023-02-01.pdf')
    print(result)

    # Retornar a lista de tuplas
    for diretorio in os.listdir('arquivos'):
        # Chama a função para mesclar os arquivos PDF no diretório fornecido
        print(sorting_files_by_date('arquivos/' + diretorio))

