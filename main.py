from functions import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Retornar a lista de tuplas
    for diretorio in os.listdir('arquivos'):
        # Chama a função para mesclar os arquivos PDF no diretório fornecido
        merge_pdfs_sorted_by_date('arquivos/' + diretorio)

