import csv
import os
from datetime import datetime

# Diretório e arquivos
diretorio = r"C:\Users\wande\OneDrive\Documentos\_01_projeto_databricks_azure\archive"

arquivo_origem = os.path.join(
    diretorio,
    "sales_transaction_v_4a_com_virgula.csv"
)

arquivo_destino = os.path.join(
    diretorio,
    "sales_transaction_v_4a_tratado_data.csv"
)

def tratar_coluna_date(arquivo_entrada, arquivo_saida):
    """
    Converte a coluna Date do formato MM/DD/YYYY
    para DD/MM/YYYY, mantendo todas as outras colunas inalteradas.
    """

    with open(arquivo_entrada, mode="r", encoding="utf-8", newline="") as csv_in:
        leitor = csv.DictReader(csv_in, delimiter=";")
        campos = leitor.fieldnames

        if "Date" not in campos:
            raise Exception("Coluna 'Date' não encontrada no arquivo.")

        with open(arquivo_saida, mode="w", encoding="utf-8", newline="") as csv_out:
            escritor = csv.DictWriter(csv_out, fieldnames=campos, delimiter=";")
            escritor.writeheader()

            for linha in leitor:
                data_raw = linha.get("Date")

                if data_raw:
                    try:
                        data_convertida = datetime.strptime(
                            data_raw.strip(),
                            "%m/%d/%Y"
                        ).strftime("%d/%m/%Y")

                        linha["Date"] = data_convertida

                    except ValueError:
                        # Se a data estiver inválida, mantém o valor original
                        pass

                escritor.writerow(linha)

    print("Tratamento da coluna Date concluído com sucesso.")
    print(f"Arquivo gerado: {arquivo_saida}")

if __name__ == "__main__":
    tratar_coluna_date(arquivo_origem, arquivo_destino)
